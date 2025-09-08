+++ 
draft = false
date = 2025-09-08T01:35:34-04:00
title = ""
description = "Adding LLM component to my blog workflow"
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

In [one of my initial blog posts](./start-simple.md), I discussed the importance of starting simple when building a new thing. This allows you to not get lost in the weeds of complexity, and, instead, think about the components that can help you achieve your goals. For each component, you can apply the same principle of starting simple. 

One of the components that I wanted to add to the workflow of my blog was the ability to automatically get a (draft) summary of a new post so that I can share it easily on social media. So, I decided to leverage a language model to help me with this task. At first, I searched for existing models. Are the small ones good enough? Can any fine-tuned small model be easily used in Github Actions without too much hassle?... but then I remembered that I should start simple! So, I just picked a LLM with free-tier API access. I then added the API key to the Github Secrets of my blog repo, and created a Github Action that would summarize a new post that is added in a PR. The action will print the summary for me. I can then do a quick review of the summary, and copy it to my social media posts! Awesome! I have now a new component in my blog workflow that helps me save time and effort! 

Can I improve this component? Sure! I can try different models, I can try to fine-tune a model, I can try to make the summary more catchy, etc. But for now, I have a working component that helps me achieve my goal of sharing my posts on social media. And I can improve it later if needed.