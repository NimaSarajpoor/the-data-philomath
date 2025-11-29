+++ 
draft = true
date = 2025-11-25T01:24:53-05:00
title = "Getting Faster RFFT in Python"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++


The **Real Fast Fourier Transform (RFFT)** converts a real-valued signal from the time domain to the frequency domain. Different libraries in Python, such as NumPy, SciPy, and [pyFFTW](https://pyfftw.readthedocs.io/en/latest/source/pyfftw/builders/builders.html), provide an API for RFFT. However, their performance can vary. pyFFTW is a Python wrapper for [FFTW](https://www.fftw.org), which is known for its speed in computing Fourier transforms. I couldn't find much documentation on how to get the best performance out of pyFFTW's RFFT. So, I decided to explore this topic and share my findings here. Let's dive in!

## Installation
[FFTW](https://www.fftw.org) is one of the requirements of pyFFTW and it does not come with pyFFTW. You can install it through `conda`. I assume you have `conda` installed, and you know how to create and activate a conda environment. See [pyFFTw's github page](https://github.com/pyFFTW/pyFFTW) to learn more about pyFFTW installation, including the minimum Python version requirement.

Once you are in your environment, install `FFTW` by running the following command:
```bash
conda install conda-forge::fftw
```

And, the other dependencies can be installed when installing pyFFTW:

```bash
conda install conda-forge::pyfftw
``` 


Now, we are ready to use pyFFTW! The following code demonstrates how to use pyFFTW to perform RFFT on a real-valued array. 

```python
import numpy as np
import pyfftw

T = np.random.rand(4)
rfft_obj = pyfftw.builders.rfft(np.empty(len(T), dtype='float64'))
R = rfft_obj(T)
```

## Performance Optimization
RFFT performance varies across input sizes. The performance of RFFT can be significantly improved when input arrays have specific sizes (e.g., powers of two). Here we consider input sizes that are powers of two, and try to find ways to improve the performance of RFFT further in those cases. 


### Timing
Let's start by preparing a script that can get the timing of RFFT computation.

```python
def _get_timing_single(n, rfft_caller, timeout=5.0, iter_max=100000):
    """
    For a single input size n, return the time taken to compute RFFT using rfft_caller
    """
    pyfftw.forget_wisdom()  # clean up any previous plans
    T = np.random.rand(n)

    R = rfft_caller(T) # dummy to create wisdom
    np.testing.assert_allclose(R, np.fft.rfft(T))  # verify correctness

    total_time = 0.0
    count = 0
    while total_time < timeout and count < iter_max:
        start_time = time.perf_counter()
        rfft_caller(T)
        total_time += time.perf_counter() - start_time
        count += 1

    return total_time / count


def get_timing(n_values, rfft_caller, timeout=5.0, iter_max=1000000, verbose=True):
    """
    n_values: an array of input sizes
    """
    timing = np.full(len(n_values), -1.0, dtype='float64')
    for i, n in enumerate(n_values):
        timing[i] = _get_timing_single(n, rfft_caller, timeout=timeout, iter_max=iter_max)
        if verbose:
            print(f"log2(n) --> {int(np.log2(n))}", flush=True)
    return timing
```

There are a few things to note in the above code:
1. To be on the safe side, we use `pyfftw.forget_wisdom()` to clear all previously-stored plans (wisdoms). This is to make sure that we start fresh and our timing result does not benefit, in any way, from any previously-computed wisdom. If you are not familiar with the concept of wisdom in FFTW, you can read more about it [on pyFFTW's documentation](https://pyfftw.readthedocs.io/en/latest/source/pyfftw/pyfftw.html#wisdom-functions).
2.  Once wisdom is obtained, it does not need to be re-computed in the same session. There is a dummy run to compute the wisdom plan in advance. Therefore, the wisdom overhead is not counted in the timing.
3. We verify the correctness of the RFFT result by comparing it with NumPy's RFFT output.


Now that we have the timing function ready, we can start exploring different implementations of RFFT using pyFFTW to see how we can improve the performance. But, first, let's prepare a script that can help us get the timing results for different implementations and plot the performance improvement.

```python
rfft_callers = {
    'V0': rfft_caller_v0,  # baseline (see below)
    # Add other versions here later
}

p_min = 2
p_max = 20
timeout = 5.0

n_values = np.power(2, np.arange(p_min, p_max + 1))

timing_results = {}
for version, caller in rfft_callers.items():
    print(f'Getting timing for {version} ...')
    timing_results[version] = get_timing(n_values, rfft_caller=caller, timeout=timeout)

plt.figure(figsize=(15, 5))
plt.title('Performance Improvement')

for version, timing in timing_results.items():
    if version == 'V0':
        plt.axhline(y=1.0, color='r', linestyle='--', label='baseline')  # baseline
    else: 
        plt.plot(
            np.arange(p_min, p_max + 1),
            timing_results['V0'] / timing,
            label=version,
            marker='o'
        )

plt.xticks(
    ticks=np.arange(p_min, p_max + 1),
    labels=np.arange(p_min, p_max + 1),
)
plt.xlabel('log2(n)')
plt.ylabel('Speed-up Factor')
plt.grid()
plt.legend()
plt.show()
```

The above code sets up a framework to compare different RFFT implementations. It defines a dictionary `rfft_callers` to hold different versions of RFFT caller functions. It then computes the timing for each version and plots the speed-up factor compared to the baseline version (V0), which is provided below. 

We are now ready to explore different implementations of RFFT using pyFFTW and see how we can improve the performance! Let's start with a baseline implementation of RFFT using pyFFTW.

### Baseline (V0)
```python
import numpy as np
import pyfftw


def rfft_caller_v0(T):
    """
    Returns the RFFT of a real-valued array T
    """
    rfft_obj = pyfftw.builders.rfft(np.empty(len(T)))
    
    return rfft_obj(T)
```

### First Attempt: Byte-align the input array in advance (V1)
`pyfftw` internally byte-aligns the input array by default to provide better performance. One potential optimization is to create a byte-aligned array in advance, and reuse this array. This allows `pyfftw` to avoid unnecessary copies of the input data that might happen within the RFFT computation.  We can also allow `pyfftw` to overwrite our array as it should not affect our original data. Here is the modified version:

```python
class rfft_caller_v1:
    def __init__(self):
        self.real_arr = None

    def __call__(self, T):
        if self.real_arr is None or len(T) != len(self.real_arr):
            self.real_arr = pyfftw.empty_aligned(len(T), dtype='float64')
        
        rfft_obj = pyfftw.builders.rfft(self.real_arr, overwrite_input=True, avoid_copy=True)
        self.real_arr[:] = T
        rfft_obj.execute()
        
        return rfft_obj.output_array
```

In this modified version, an instance of the class `rfft_caller_v1` can be used to compute the RFFT. It holds the byte-aligned array `real_arr`, as an attribute, after the first call. When the `__call__` method is invoked again, it checks if the size of the input array `T` matches the size of the existing aligned array, and if yes, it reuses the existing byte-aligned array. Also, note that we intentionally do not save the RFFT object as attribute and do not use it across multiple calls in this version. We will explore that in a later version. Let's update the dictionary `rfft_callers` to include this new version:

```python
rfft_callers = {
    'V0': rfft_caller_v0,
    'V1': rfft_caller_v1(),
}
```

Let's check out the performance improvement:

![Performance Gain](Figure_Performance_V1.png)

As shown in the performance plot above, our first attempt to optimize the RFFT computation resulted in 5-10% speed-up for most cases. Not bad for a first try! Let's see if we can do better!!

### Second Attempt: Use pyfftw.FFTW object directly (V2)
Another idea to explore is to use the `pyfftw.FFTW` object directly instead of using the builder function. The builder function `pyfftw.builders.rfft` is a convenient way to create FFTW objects. This may introduce some overhead. So, on top of the previous optimization, we are going to use `pyfftw.FFTW` directly.

```python
class rfft_caller_v2:
    def __init__(self):
        self.real_arr = None
        self.complex_arr = None
    
    def __call__(self, T):
        if self.real_arr is None or len(T) != len(self.real_arr):
            self.real_arr = pyfftw.empty_aligned(len(T), dtype='float64')    
            self.complex_arr = pyfftw.empty_aligned(len(T) // 2 + 1, dtype='complex128')  

        rfft_obj = pyfftw.FFTW(
            self.real_arr,
            self.complex_arr,
            direction='FFTW_FORWARD',
            flags=('FFTW_MEASURE', 'FFTW_DESTROY_INPUT'),
            threads=1,
        )    
        self.real_arr[:] = T
        rfft_obj.execute()

        return self.complex_arr
```

Note that, in addition to the input array, we also created an output array `complex_arr` to hold the RFFT result. Let's update the dictionary `rfft_callers` to include this new version:

```python
rfft_callers = {
    'V0': rfft_caller_v0,
    'V1': rfft_caller_v1(),
    'V2': rfft_caller_v2(),
}
```

![Performance Gain](Figure_Performance_V2.png)

As shown in the performance plot above, using `pyfftw.FFTW` directly resulted in a significant performance improvement compared to the previous version. We achieved about 2.5x speed-up for short-size arrays (arrays with lengths `<2^7`), and around 1.5x speed-up for larger arrays, where the length of arrays is `>2^15`. For array sizes in between, we observed that the speed-up is less than 25% for most cases. 

### Third Attempt: Reuse the RFFT object (V3)
In the previous version, we intentionally created the RFFT object inside the `__call__` method. This means that for every call, a new RFFT object is created. The goal here is to see how much performance gain we can get by reusing the RFFT object across multiple calls when the input size does not change.

```python
class rfft_caller_v3:
    def __init__(self):
        self.real_arr = None
        self.complex_arr = None
        self.rfft_obj = None
    
    
    def __call__(self, T):
        if self.real_arr is None or len(T) != len(self.real_arr):
            self.real_arr = pyfftw.empty_aligned(len(T), dtype='float64')    
            self.complex_arr = pyfftw.empty_aligned(len(T) // 2 + 1, dtype='complex128')

            self.rfft_obj = pyfftw.FFTW(
                    self.real_arr,
                    self.complex_arr,
                    direction='FFTW_FORWARD',
                    flags=('FFTW_MEASURE', 'FFTW_DESTROY_INPUT'),
                    threads=1,
                ) 
           
        self.real_arr[:] = T
        self.rfft_obj.execute()

        return self.complex_arr
```

Let's update the dictionary `rfft_callers` to include this new version:

```python
rfft_callers = {
    'V0': rfft_caller_v0,
    'V1': rfft_caller_v1(),
    'V2': rfft_caller_v2(),
    'V3': rfft_caller_v3(),
}
```

![Performance Gain](Figure_Performance_V3.png)

As shown in the performance plot above, reusing the RFFT object resulted in a huge performance improvement compared to the previous versions. We achieved about 30x speed-up for arrays with lengths `<2^8`. And from that point on, the speed-up gradually decreases to around 2x-3x for larger arrays`. This shows the overhead of creating RFFT object is considerable even when plan (wisdom) is already available. 

If the goal is to compute RFFT on multiple arrays with the same size, reusing the RFFT object is straightforward. You only create it once (in which the plan is computed as well), and then you can use it multiple times without any overhead of creating the RFFT object again. However, if the input sizes vary a lot, and you need to compute RFFT on arrays with a certain, different sizes sequentially, and do that again and again, then caching the RFFT objects for different sizes can significantly improve performance. However, this requires more work to implement the caching mechanism, and it requires more memory to store the cached RFFT objects. This is outside the scope of this post.

## Conclusion
In this post, we explored different ways to optimize the performance of RFFT computation using pyFFTW in Python. We started with a baseline implementation and gradually improved it by applying various optimizations, such as byte-aligning the input array, using the `pyfftw.FFTW` object directly, and reusing the RFFT object across multiple executions. We haven't exploredmulti-threading in this post, but it can be another avenue for performance improvement, especially for large arrays.