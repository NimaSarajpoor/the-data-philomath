+++
date = '2025-08-31T20:08:14-04:00'
draft = false
title = "Let's join tables.... wait!"
+++

Suppose you are working on a project and you have access to two data sets coming from upstream jobs. For each data set, you should know what each row represents and what is the row identifer. However, unfortuantely, such information is not always available. So, you may need to do some analysis to understand whether a certain logic works or not. Suppose the data set 1 has the columns `X, A, B` and the data set 2 has the columns `X, C, D`. And you are told that you can join the two data sets using `X` as the key to find the value of the feature `C` for each of the reocrd in the data set 1. Can I join? What can go wrong? This can go wrong if there is no 1-1 mapping between the columns `X` and `C`. For instance, the data set 2 might look like this:

```raw
X   C   D
1   5   9
1   6   10
2   7   11
```

Here, joining can create duplicate rows in the resulting dataset, which may not be desirable depending on the analysis you want to perform. How can you check if what kind of mapping exists between two columns `X` and `C`? 

```python
def _get_mapping(df, i, j):
    """
    mapping FROM column i TO column j
    """
    col1 = df.columns[i]
    col2 = df.columns[j]
    mapping_type = None

    if df.groupby(col1)[col2].nunique().max() == 1:
        out = '11'
    else:
        out = '1M'

    return out


def analyze_mapping(df):
    mapping_type = None
    n = len(df.columns)
    mapping = np.empty((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            mapping[i, j] = _get_mapping_type(df, i, j)

    return mapping
```

Next time that you need to join two DataFrames, make sure to analyze the mapping between the key columns first. This will help you understand the potential impact of the join operation on your data and avoid unexpected results. If it has one to many mapping, you may end up with duplicate rows in the resulting DataFrame, which could affect your analysis. In such case, you may need to aggregate the data or think about how to handle the duplicates. Always check the mapping before performing joins!