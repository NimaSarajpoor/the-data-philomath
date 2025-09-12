+++ 
draft = false
date = 2025-09-12T00:13:52-04:00
title = "Quick overview of different types of `mean` in investment"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

In investment, the term "mean" can refer to different types of averages that are used to analyze and interpret financial data. Here are some common types of means used in investment:

## Arithmetic Mean
This is the most straightforward type of mean, calculated by adding up all the values and dividing by the number of values. For instane, it can be used to calculate a stock's average closing price over a specific period, like a month or a year.

## Geometric Mean
This mean is calculated by multiplying all the values together and then taking the nth root (where n is the number of values). The geometric mean is particularly useful for calculating average returns over multiple periods, as it accounts for compounding effects. For example, if an investment grows by 10% one year and 20% the next, the geometric mean provides a more accurate representation of the average growth rate than the arithmetic mean.

$ \text{Geometric Mean} = \sqrt[n]{x_1 \cdot x_2 \cdot \ldots \cdot x_n} $ 

In the example above, the geometric mean of the returns would be:

$ \text{Geometric Mean} = \sqrt[2]{(1 + 0.10) \cdot (1 + 0.20)} - 1 = \sqrt[2]{1.10 \cdot 1.20} - 1 \approx 0.15$

Note that we add 1 to each return as that is the actual factor between the initial and final value! For the example above:

$FV1 = PV * (1 + 0.1)$ <br>
$FV2 = FV1 * (1 + 0.2)$ <br>

$FV2 = PV * (1 + 0.1) * (1 + 0.2)$ <br>

And if `R` is the average growth factor, it basically means: <br>
$FV2 = PV * (1 + R)^{2}$ <br>

And from there, you can derive the formula for the geometric mean!

## Harmonic Mean 
This mean is calculated by taking the reciprocal of the arithmetic mean of the reciprocals of the values. The harmonic mean is useful when dealing with rates or ratios, such as price-to-earnings (P/E) ratios.

$ \frac{1}{\text{Harmonic Mean}} = \frac{1}{n}\left({\frac{1}{x_1} + \frac{1}{x_2} + \ldots + \frac{1}{x_n}}\right)$

Example: Suppose an investor buys $100 of a security each month for n = 2 months. The share prices are $10 and $20 at the two purchase dates. What is the average price paid for the security?

* month 1: With $100 and a share price of $10, the investor buys 10 shares at $10 each.
* month 2: With $100 and a share price of $20, the investor buys 5 shares at $20 each.

To find the average price paid, we need to calculate the total amount invested and the total number of shares purchased:

Total amount invested = $100 + $100 = $200
Total shares purchased = 10 + 5 = 15

Average price paid = Total amount invested / Total shares purchased
Average price paid = $200 / 15 ≈ $13.33
