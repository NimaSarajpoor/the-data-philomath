+++ 
draft = true
date = 2025-09-02T20:34:34-04:00
title = "Batch processing"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++


## Batch Processing

A data pipeline is a series of data processing steps that involve the collection, transformation, and storage of processed (curated) data. Suppose that there is an upstream data source that is updated on daily basis. The data is tabular and has the following columns:
* UserId
* VisitId
* Action
* OriginalTimestamp
* IngestedTimestamp

The `Action` column represents the type of user action that occurred, such as "click", "view", or "purchase". Let's say the downstream job is simple: For records with same UserId, VisitId, we want to collect the actions. So, the main column of the curated data should include at least the following columns:

* UserId
* VisitId
* Actions (a list of all actions taken during the visit)


**Now, let's ask a few questions:**

1. What if you do not want to lose the `OriginalTimestamp` information?
<br>
One approach is to get the minimum and maximum `OriginalTimestamp` for each group of records with the same UserId, VisitId. This way, you can retain the time range of the user's visit while still curating the data. 

2. What column should be used for slicing the data for batch processing?
<br>
There are two options: `OriginalTimestamp` and `IngestedTimestamp`. What can go wrong with each option? For the `OriginalTimestamp`, if the upstream data source has late-arriving data (i.e., data that arrives after the expected time), using `OriginalTimestamp` for slicing could lead to missing or incomplete data in the curated dataset. For example, if a record with an `OriginalTimestamp` of yesterday arrives today, it would not be included in the batch for yesterday if you are slicing by `OriginalTimestamp`. On the other hand, using `IngestedTimestamp` can help ensure that all data that has been ingested up to a certain point is included in the batch. However, this approach may lead to overlapping data if records with the same `OriginalTimestamp` are re-ingested at different times. This could result in duplicate records in the curated dataset if not handled properly. 

3. What happens if only some of records with same `(UserId, VisitId)` are available in the upstream data source, and the other records with same `(UserId, VisitId)` arrive later?
<br>
In this case, the curated dataset may be incomplete for that particular `(UserId, VisitId)` pair. If the downstream job is designed to process all actions for a given visit, it may miss some actions if they arrive after the batch has been processed. One way to handle this is to implement a mechanism for late-arriving data, such as re-processing the batch when new data arrives or using a more flexible data model that can accommodate updates to existing records. You can think about it further and ask: "is there a reason why some records are late-arriving?" After checking out the data, you may notice that the maximum `OriginalTimestamp` for a given `IngestedTimestamp` is at 00:00 UTC. This means that the upstream job simply breaks the records and ingests them in separate batches based on their `IngestedTimestamp`, which can lead to the observed late-arriving records. What they could have done is to revise the ingestion strategy to account for records that are with same `UserId, VisitId` but after 00:00 UTC (in the next day). 

Most teams rely on a combination of both `OriginalTimestamp` and `IngestedTimestamp` for their batch processing needs. They may use `OriginalTimestamp` for initial data ingestion and processing, while also implementing mechanisms to handle late-arriving data based on `IngestedTimestamp`. This hybrid approach allows them to balance the need for accurate event timing with the practicalities of data ingestion and processing delays. 


## Test
Unfortunately, there are many teams that do not write proper tests for their batch processing pipelines. This can lead to a variety of issues, including undetected bugs, data quality problems, and difficulties in maintaining and evolving the pipeline over time. Writing tests for batch processing jobs can be challenging due to the complexity of the data and the need to simulate various scenarios, such as late-arriving data or missing records. However, it is essential to invest in testing to ensure the reliability and robustness of the data pipeline. Some best practices for testing batch processing jobs include:

1. **Unit Tests**: Write unit tests for individual components of the pipeline, such as data transformation functions or aggregation logic. These tests should cover a range of input scenarios, including edge cases.

2. **Integration Tests**: Implement integration tests that validate the end-to-end behavior of the pipeline. These tests should run against a representative dataset and verify that the output matches the expected results.

3. **Data Quality Checks**: Incorporate data quality checks into the pipeline to catch issues early. This can include validating schema, checking for null values, and ensuring data consistency.

4. **Monitoring and Alerting**: Set up monitoring and alerting for the batch processing jobs to detect failures or performance issues in real-time. This can help teams respond quickly to problems and minimize the impact on downstream consumers.

5. **Documentation**: Maintain clear documentation for the batch processing pipeline, including data sources, transformations, and dependencies. This can help new team members understand the pipeline and facilitate testing efforts.

By prioritizing testing and quality assurance, teams can build more reliable batch processing pipelines that deliver accurate and timely data to their stakeholders.


**Let's write a test for the batch processing pipeline!**
We first need to understand what we want to test! The process is as follows: <br>
`data -> logic -> curated data` <br>

I can first create a data that contains several records with different `UserId` and `VisitId` pairs, as well as varying `OriginalTimestamp` and `IngestedTimestamp` values. This will allow me to test how the batch processing pipeline handles different scenarios, such as late-arriving data and missing records. For the sake of simplicity, I've ignored the column `Action`. All I want is to count rows with similar `(UserId, VisitId)` pairs. We can then compare the results of the full dataset with the results obtained from processing the data in batches.

```python
import pandas as pd
from datetime import datetime


def test_batch_processing():
    # Create a sample dataset
    data = [
        {"UserId": 1, "VisitId": 101, "OriginalTimestamp": datetime(2023, 1, 1, 23, 55), "IngestedTimestamp": datetime(2023, 1, 2, 0, 0)},
        {"UserId": 1, "VisitId": 101, "OriginalTimestamp": datetime(2023, 1, 1, 23, 55), "IngestedTimestamp": datetime(2023, 1, 2, 0, 0)},
        {"UserId": 1, "VisitId": 102, "OriginalTimestamp": datetime(2023, 1, 1, 23, 57), "IngestedTimestamp": datetime(2023, 1, 2, 0, 0)},
        {"UserId": 1, "VisitId": 102, "OriginalTimestamp": datetime(2023, 1, 1, 23, 58), "IngestedTimestamp": datetime(2023, 1, 2, 0, 0)},
        {"UserId": 2, "VisitId": 201, "OriginalTimestamp": datetime(2023, 1, 1, 23, 59), "IngestedTimestamp": datetime(2023, 1, 2, 0, 0)},
        {"UserId": 2, "VisitId": 201, "OriginalTimestamp": datetime(2023, 1, 2, 0, 1), "IngestedTimestamp": datetime(2023, 1, 3, 0, 0)},
        {"UserId": 2, "VisitId": 201, "OriginalTimestamp": datetime(2023, 1, 2, 0, 2), "IngestedTimestamp": datetime(2023, 1, 3, 0, 0)},
    ]
    df = pd.DataFrame(data)

    # logic: group by UserId and VisitId, and counts records
    
    # ref
    # perform logic on full data `df`
    ref = df.groupby(["UserId", "VisitId"]).size()
    
    # comp
    # perform logic on full data `df` but in two batches
    batch1 = df[df.IngestedTimestamp == datetime(2023, 1, 2, 0, 0)]
    batch2 = df[df.IngestedTimestamp == datetime(2023, 1, 3, 0, 0)]

    comp1 = batch1.groupby(["UserId", "VisitId"]).size()
    comp2 = batch2.groupby(["UserId", "VisitId"]).size()
    comp = pd.concat([comp1, comp2], axis=0)
    
    # compare comp with ref
    pd.testing.assert_series_equal(ref, comp)
```

And you can easily see that this fails! We may need to adjust the batch processing logic to ensure that it correctly handles late-arriving data. We can add more tests too to cover different scenarios. If the tests are not added, the quality of the code may suffer, and potential issues could go unnoticed. It's crucial to prioritize testing and quality assurance in any data processing pipeline!