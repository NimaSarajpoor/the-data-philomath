+++
date = '2025-08-29T00:22:30-04:00'
draft = false
title = 'Minimal Reproducible Example'
+++

Minimal Reproducible Example (MRE) is a complete, self-contained, and executable code snippet designed to demonstrate and reproduce a specific problem, bug, or unexpected behavior. I think this is one of the key pillars of having effective communications between two teams who are accountable for different pieces of a process. 

Suppose team A has a pipeline that reads input data and writes output data to a certain location consumed by a pipeline of team B. Team B notices an issue in the output of their pipeline. Team B conducts an investigation and realizes there is a certain issue in the data they consume. How should they report it to team A? One approach is to just tell team A: "There are duplicate records with the data you provided." However, this statement is vague and does not provide enough context for team A to understand the problem. This can become difficult to understand if there are multiple outputs and the duplicated records are observed when two or more data are combined. Also team B might be reading the data from an old location!! To avoid all these ambiguities, team B should create a Minimal Reproducible Example (MRE) that clearly demonstrates the issue. The MRE should include the important pieces to clearly demonstrate the issue. For instance, it can be a short code snippet that reproduces the issue. It should contain the location of data and a simplified version of logic to show the issue. In some cases, adding the versions of libraries used can also be helpful. The advantage of having MRE is that other teammates can easily understand the problem and potentially reproduce it in their own environment, which can facilitate faster debugging and resolution.
