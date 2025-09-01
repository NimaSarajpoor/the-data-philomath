+++ 
draft = false
date = 2025-08-31T23:49:57-04:00
title = "Right Chart, Right Time"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

In today's data-driven world, the ability to visualize data effectively is crucial. Choosing the right chart type can make all the difference in conveying your message clearly and accurately. In this post, I've shared a personal experience where selecting the appropriate chart transformed the way I presented data insights.

## Example 1: the  data pipelines
Imagine you are working on a project that involves monitoring several data pipelines. And there is a dependency between these pipelines. For instance, pipleine D depends C, and the pipeline C depends on A and B. We want to deomonstrate if the current settings work properly and each pipeline is executed at a proper time. To this end, you can use a [Gantt chart](https://plotly.com/python/gantt/) to visualize the execution timeline of each pipeline while considering their dependencies.


## Example 2: the data volume in different days
Suppose that you have a data set that is updated daily, and you want to visualize the number of records per day. One way is to use a line chart to show the trend of data volume over time. This can help identify patterns, such as peak usage days or anomalies in data collection. Let's say you want to see if there is any relationship between the daily volume of data changes and the day of the week. In this case, a [calplot](https://pypi.org/project/calplot/) might be useful to visualize the data in a more compact form and show the values with respect to the day of the week. 