+++ 
draft = true
date = 2025-12-07T20:11:47-05:00
title = "Explore pyFFTW Wisdom: Understanding FFTW Plans in Python"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++


In this post, I share some insights I learned while working with the [pyFFTW](https://github.com/pyFFTW/pyFFTW) library in Python, specifically about the concept of [wisdom](https://pyfftw.readthedocs.io/en/latest/source/tutorial.html#wisdom). pyFFTW is a Python wrapper around [FFTW](http://www.fftw.org/), a highly-optimized library for computing the fourier transform. One of FFTW’s features is its ability to store and reuse optimized FFT plans, collectively referred to as wisdom. This post focuses on explaining what wisdom is and how it works.


## What is `wisdom`?

According to the [pyFFTW documentation](https://pyfftw.readthedocs.io/en/latest/source/tutorial.html#wisdom):

> When the a particular transform has been created, distinguished by things like the data type, the shape, the stridings and the flags, FFTW keeps a record of the fastest way to compute such a transform in future. This is referred to as wisdom. 

It is important to understand that `wisdom` is about the planning of FFT computations, not the intermediate results or transformations. The planning process to obtain wisdom is only for the first time. The subsequent calls will skip the planning part once the `wisdom` becomes available.

How to verify that `wisdom` works? We can create an object from the class `pyfftw.FFTW`, and call it. This will create the plan. Then, in the same session, we can create another object but use the flag `FFTW_WISDOM_ONLY`, which tells the library to only use the existing `wisdom`. If the `wisdom` is not available, the second object should raise an error. 

```python
import pyfftw
import numpy as np

# Create some data
n = 2 ** 10
a = pyfftw.empty_aligned(n, dtype='complex128')
b = pyfftw.empty_aligned(n, dtype='complex128')

# First FFTW object with planning
fft_obj = pyfftw.FFTW(a, b, flags=('FFTW_MEASURE',))
fft_obj()  # This will create the plan and compute the FFT

a_new = pyfftw.empty_aligned(n, dtype='complex128')
b_new = pyfftw.empty_aligned(n, dtype='complex128')
fft_obj_new = pyfftw.FFTW(a_new, b_new, flags=('FFTW_WISDOM_ONLY',))
fft_obj_new()  # This should work since wisdom is available
```

Note that we used the flag `FFTW_MEASURE` in the first object to create the plan. In fact, that is the default flag used by pyFFTW when creating an FFTW object. Different flags can be used to control the planning process, such as `FFTW_ESTIMATE`, `FFTW_PATIENT`, and `FFTW_EXHAUSTIVE`. The choice of flag can affect the time taken to create the plan and the efficiency of the resulting FFT computation. Exploring the impact of different flags on planning time and performance is out of the scope of this post.



## `wisdom` vs `plan`

The documentations says:

> When the program is completed, the wisdom that has been accumulated is forgotten.

To better understand `accumulated wisdom`, we need to distinguish between `wisdom` and `plan`. A `plan` refers to a specific optimized strategy for computing a particular FFT operation. In contrast, `wisdom` encompasses a collection of such plans that have been accumulated over time for various FFT configurations.

How to verify the wisdom has the accumulated plans? Let's create two FFTW objects with different sizes and verify if the planning for the first one is available!

```python
import pyfftw
import numpy as np

# Create some data
n1 = 2 ** 10
a1 = pyfftw.empty_aligned(n1, dtype='complex128')
b1 = pyfftw.empty_aligned(n1, dtype='complex128')
fft_obj_1 = pyfftw.FFTW(a1, b1, flags=('FFTW_MEASURE',))
fft_obj_1()  # Create plan for size n1

n2 = 2 ** 12
a2 = pyfftw.empty_aligned(n2, dtype='complex128')
b2 = pyfftw.empty_aligned(n2, dtype='complex128')
fft_obj_2 = pyfftw.FFTW(a2, b2, flags=('FFTW_MEASURE',))
fft_obj_2()  # Create plan for size n2

# Now, let's create FFTW objects with WISDOM_ONLY flag
a_new = pyfftw.empty_aligned(n1, dtype='complex128')
b_new = pyfftw.empty_aligned(n1, dtype='complex128')
fft_obj_new = pyfftw.FFTW(a_new, b_new, flags=('FFTW_WISDOM_ONLY',))
fft_obj_new()  # This should work since wisdom is available
```

## Export and Import `wisdom`

According to [the documentation](https://pyfftw.readthedocs.io/en/latest/source/tutorial.html#wisdom), the `wisdom` is forgotten when the program ends. This means that if you restart your Python session, the `wisdom` will not be available anymore. To avoid losing the `wisdom` across sessions, you need to export, and save it to a file so that you can use it in the next session. Again, note that the `wisdom` can be a collection of plans. So, if you want to save them all, you can export at the end of your program. You can then save it to a file, and load it in the next session. You just need to import it once at the beginning of your program. Then, pyfftw will have access to all the previously-computed plans. 

How to verify this?  Let's create a simple example where we create two FFTW objects, call them to create plans, and then save the `wisdom`. In a new session, we then load the `wisdom` and verify that the plan is available.

```python
# First session: create plans and save wisdom
import pickle
import pyfftw
import numpy as np

n1 = 2 ** 10
a1 = pyfftw.empty_aligned(n, dtype='complex128')
b1 = pyfftw.empty_aligned(n, dtype='complex128')

fft_obj_1 = pyfftw.FFTW(a1, b1, flags=('FFTW_MEASURE',))
fft_obj_1()  # Create plan

n2 = 2 ** 12
a2 = pyfftw.empty_aligned(n2, dtype='complex128')
b2 = pyfftw.empty_aligned(n2, dtype='complex128')
fft_obj_2 = pyfftw.FFTW(a2, b2, flags=('FFTW_MEASURE',))
fft_obj_2()  # Create plan

# Export wisdom
wisdom = pyfftw.export_wisdom()
with open('fftw_wisdom.pkl', 'wb') as f:
    pickle.dump(wisdom, f)
```

and then in a new session:

```python
# Second session: load wisdom and verify plans
import pickle
import pyfftw
import numpy as np

# Load wisdom
with open('fftw_wisdom.pkl', 'rb') as f:
    wisdom = pickle.load(f)
pyfftw.import_wisdom(wisdom)

n = 2 ** 10
a = pyfftw.empty_aligned(n, dtype='complex128')
b = pyfftw.empty_aligned(n, dtype='complex128')
fft_obj = pyfftw.FFTW(a, b, flags=('FFTW_WISDOM_ONLY',))
fft_obj()  # This should work since wisdom is imported
```


## `wisdom` is platform dependent

Note that `wisdom` may not be portable across different platforms. The plans generated by FFTW are specific to the hardware and software environment in which they were created. How to check this? The best way is to export the `wisdom` on one system and import it on another with a different architecture or OS.


## Conclusion
In this post, I explained the concept of `wisdom` in the pyFFTW library. One important takeaway is that `wisdom` is about the planning of FFT computations, not the intermediate results or transformations. Exporting `wisdom` can help save time in future sessions by reusing previously computed plans. This can be particularly beneficial in applications that require a certain set of fourier transforms.


