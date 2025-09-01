+++ 
draft = false
date = 2025-09-01T00:25:41-04:00
title = "The Time Value of Money"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

In finance, the concept of the time value of money (TVM) is fundamental. It asserts that a sum of money has a different value today than it will in the future. This principle is crucial for making informed investment decisions and understanding the true cost of borrowing.

## Key Components of TVM

1. **Present Value (PV)**: The current worth of a future sum of money, discounted at a specific interest rate.
2. **Future Value (FV)**: The value of a current asset at a future date based on an assumed rate of growth.
3. **Interest Rate (r)**: The rate (e.g. `0.02`) at which money grows over time in a certain period.
4. **Number of Periods (N)**: The number of periods for which the money is invested or borrowed.

## The TVM Formula

The basic formula for calculating the future value of an investment is $FV = PV \times (1 + r)^N$; where, $(1+r)^{N}$ is the future value factor

Conversely, to find the present value, the formula is: $PV = FV(1 + r)^{-N}$; where, $(1 + r)^{-N}$ is the present value factor.

## Interest Rate (r)

The interest rate (r) can be seen in three ways:
1. The minimum rate of return an investor must receive in order
to accept the investment
2. The discount rate used to determine the present value of future cash flows
3. The opportunity cost, i.e. the value the investors forgo by choosing a different route for their money.

The interest rate (r) is composed of several factors:
* the real risk-free interest rate
* the inflation premium
* the default risk premium
* the liquidity premium
* the maturity premium

[!NOTE]  
The sum of `the real risk-free interest rate` and `the inflation premium` is known as `the nominal risk-free interest rate`.


## Example on TVM
Suppose you want to invest $100 today for two years with an annual interest rate of 5%. Let's see how much money you will have in the future.

Using the future value formula:

$ FV = PV \times (1 + r)^N $

Where:
- PV = $100
- r = 0.05
- N = 2

Plugging in the values:

$ FV = 100 \times (1 + 0.05)^2 $ <br>
$ FV = 100 \times (1.1025) $ <br>
$ FV = 110.25 $

To break it down:
1. In the first year, the investment grows to $100 \times (1 + 0.05) = $105.
2. In the second year, the investment grows to $105 \times (1 + 0.05) = $110.25.

Note that, in the second year, you earn interest not only on your initial investment but also on the interest that was added in the first year. This is the essence of compound interest and the time value of money.

## Drawing timeline

<div style="font-family: monospace;">
0───1───2─── ... ───N
</div>

Now, if you invest `PV` amount in the beginning of a year, and want to know the FV at the end of the second year, you can take a look at the timeline, and compute the FV as follows:

* $FV_{1} = PV \times (1 + r)$ <br>
* $FV_{2} = FV_{1} \times (1 + r) = PV \times (1 + r)^2$


## Non-annual compounding

In the real world, interest might be compounded more frequently than annually (e.g., monthly, quarterly). The formulas can be adjusted to account for these different compounding periods.

$FV_{N} = PV \times (1 + \frac{r}{m})^{Nm}$

where,
- $m$ is the number of compounding periods per year (e.g., 12 for monthly, 4 for quarterly).
- $N$ is the total number of years the money is invested or borrowed.
- $r$ is the stated annual interest rate compounded monthly/quarterly.


[!NOTE]
You may read "4% stated annual interest rate compounded quarterly". This means the interest rate in a quarter is 1% (i.e., 4% divided by 4). So, if I have five quarters in mind, then $FV=PV(1+0.01)^{5}$.


## Continuous Compounding
In continuous compounding, interest is calculated and added to the principal continuously, rather than at discrete intervals. The formula for continuous compounding is:

$FV = PV \times e^{rN}$


## Effective Annual Rate (EAR)
The Effective Annual Rate (EAR) is the interest rate on an investment or loan that is compounded over a given period, expressed as an annual rate. In other words:

$ PV(1 + \frac{r}{m})^{m * 1} = PV(1 + EAR)$

So:

$EAR = (1 + \frac{r}{m})^{m} - 1$


## Present/Future Value of a Series of Cash Flows

When dealing with multiple cash flows, such as regular investments or payments, the TVM formulas can be adapted to account for these series of cash flows.

There are different kinds of cash flows:
* Annuities: Regular, fixed payments made over time (e.g., monthly rent).
    * Ordinary Annuity: Payments made at the end of each period.
    * Annuity Due: Payments made at the beginning of each period.
* Perpetuities: Cash flows that continue indefinitely (e.g., preferred stock dividends).

Let's start with `Perpetuities`. Let's say there is a regular cash flow of $C$ that continues forever. And let's say the payment starts at the end of each year. Let's add them together at `t=0`:

$PV = C(1+r)^{-1} + C(1+r)^{-2} + C(1+r)^{-3} + ... $

$PV = \frac{C(1+r)^{-1}}{1 - (1+r)^{-1}}$

$PV = \frac{C}{r}$


This is an important relationship. I can use it to compuate PV/FV for annuities. Let's say I have an ordinary annuity and I am paid `A` amount at the end of each year for N years. How can I calculate its present value? I can see it as a combination of two perpetuities. One is a perpetuity with amount `A` that starts at the end of year `N + 1`, and the other is a perpetuity that starts at the end of year 1.

So the present value of the annuity can be calculated as:

$PV = \frac{A}{r} - \frac{A}{r}(1 + r)^{-N}$

And for annuity due, the difference is that the payments are made at the beginning of each period. So, the last payment will be at times `t0`, `t1`, ..., and `t19`. Let's compute the present value for annuity due by breaking it down into two parts:
* A present value of `A` at t=0
* An ordinary annuity that starts at t=1 and lasts for `N-1` periods.

$PV = A + \left(\frac{A}{r} - \frac{A}{r}(1 + r)^{-N}\right)$

