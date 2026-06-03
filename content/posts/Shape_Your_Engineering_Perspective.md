+++
date = '2026-06-02T11:18:00-04:00'
draft = false
title = 'Shape Your Engineering Perspective!'
+++

The GitHub repository [hacker-laws](https://github.com/dwmkerr/hacker-laws) provides a collection of "laws" that describe various phenomena in the world of technology, programming, and software development. After reading through the repository, I found that many of the laws resonated with my personal experiences in both personal and non-personal projects. I've shared below some of the laws that I found particularly relevant.

1. Dunning–Kruger effect

    This rule says that you do not know what you do not know! So, if you are incompetent in a certain area, you can't know you're incompetent. The skills you need to produce a right answer are exactly the skills you need to recognize what a right answer is! 

    Suppose you are put in charge of modifying a piece of a project due to platform changes. The best thing to do is to collect information about the project and the platform changes, and understand their impact. The worst thing that can happen is to assume that impact is minimal and start modifying the project without understanding the full scope of the changes. This can lead to a lot of wasted time and effort, as well as potential bugs and issues. And if someone says: "It is just a small change, it won't affect much. You should be able to deliver it in 1 month", you should be cautious unless you know the person is an expert in the area. 


2. Broken windows theory

    This rule highlights that lack of care in an environment leads to further deterioration of that environment! I noticed this in both the codebase and the documentation. If there are a lot of silent bugs in the codebase and they are not addressed, it can lead to more bugs being introduced, as developers may not take the time to properly test and debug their code. Similarly, if documentation is not well-maintained, it can lead to confusion and misunderstandings among team members, which can further deteriorate the quality of the project! 

    Some people may argue that "we don't have time to fix all the bugs, we need to focus on delivering new features". However, this can lead to a vicious cycle where the codebase becomes increasingly buggy and difficult to maintain, which can ultimately slow down development and make it harder to deliver new features in the long run. It's important to strike a balance between fixing bugs and delivering new features, and to prioritize addressing critical issues that can impact the overall quality of the project. Although you may hear "Tech Debt", it is important to understand that it is not just a technical issue, but also a cultural issue that needs to be addressed and will help the team to be more efficient and productive in the long run!


3. Brook's Law

    This rule states that adding more people may result in less productivity! I was in charge of a project and a new resource was added. The new resource was not familiar with the project and had to spend a lot of time getting up to speed. I had no idea about their skills and experience, and I assumed that they would be able to contribute immediately. However, it turned out that they needed a lot of guidance and support, which took up a lot of my time and resources. This ultimately slowed down the progress of the project, and I finally had to take on more of the work myself to meet the deadlines. This experience taught me that adding more people to a project does not always lead to increased productivity, and that it's important to carefully consider the skills and experience of new team members before bringing them on board. It's also important to provide adequate training and support to new team members to help them get up to speed quickly and contribute effectively to the project!


4. The KISS principle

    This rule simply says: "Keep it simple, stupid!" When I was trying to set up a website for myself, I wanted to use a complex framework that had a lot of features and capabilities. I wanted to impress others with my technical skills and create a website that was visually stunning and had a lot of components, like getting feedback from readers, showing the most popular posts, etc. However, I quickly realized that this approach was not sustainable, and it was taking a lot of time and effort to maintain the website. I also had to take into account the fact that I had limited resources and time to dedicate to the project, and that I needed to prioritize my efforts on what was most important to me, which was to share my thoughts and ideas with others! So, I decided to focus on finding a way to allow me to publish my post by simply writing a markdown file and pushing it to a repository! I kept it simple and focused on the core functionality that I needed. I wrote about it in my blog post [start-simple](https://the-data-philomath.netlify.app/posts/start-simple/)!

5. Goodhart's Law

    At its core, the law states that "When a measure becomes a target, it ceases to be a good measure." A codebase that I was working on needed to be checked via an automation process, which meant that we had to meet certain metrics in order to pass the checks. Test and Coverage were two of the metrics that we had to meet. However, I noticed that some tests were not actually testing anything meaningful, and they were there to increase the coverage percentage! 

6. Input-Process-Output (IPO)

    A system can be described simply as: `input(s) --> process(es) --> output(s)`. To understand the system, one needs to take a step back and look at the big picture. 
    
    
    For instance, if you are running a job in the cloud, your system can include:
    - The data that you are using (input)
    - The time of processing (input)
    - The (parameter, value)s that you are using (input)
    - The code that you are running (process)
    - The platform that you are running on (process)
    - The compute resources (their size) (process)
    - The versions of libraries and their dependencies (process)
    - The output of the job (output)

    Or, if you are working on a project, your system can include:
    - The project requirements (input)
    - The project design (process)
    - The project implementation (process)
    - The project testing (process)
    - The project deployment (process)
    - The project maintenance (process)
    - The application / documentation (outputs)


7. Linus's Law

    > This law simply states that the more people who can see a problem, the higher the likelihood that someone will have seen and solved the problem before, or something very similar.

    One of the main problems that I noticed is that lack of collaboration and interest in reviewing others' work. This can lead to a situation where a problem is not being solved because no one has seen it before, and no one is interested in solving it. This can lead to a lot of wasted time and effort, as well as potential bugs and issues. It's important to encourage collaboration and interest in reviewing others' work, as this can help to increase the likelihood that problems will be solved quickly and efficiently! Also, it helps to create a culture of learning and sharing knowledge, which can lead to a more productive and efficient team overall! Furthermore, it allows a team member to handle a critical bug even if the person who developed or reported the bug is not available.


8. Law of the instrument

    This law states that "If all you have is a hammer, everything looks like a nail." I have noticed this in my work, where I tend to rely on a specific tool or technology that I am familiar with, even when it may not be the best fit for the task at hand. This can lead to suboptimal solutions and can limit my ability to effectively solve problems. It's important to be aware of this bias and to be open to exploring different tools and technologies that may be better suited for the task at hand. By doing so, I can expand my skill set and become more versatile in my problem-solving abilities!

9. The Robustness Principle (Postel's Law)

    It says:
    > "Be conservative in what you do, be liberal in what you accept from others." 

    I realized that this can be an important principle to follow when processing
    data managed by external sources. Suppose that you are working on a project that relies on columns A and B from an external data source. If you are conservative in what you do, you will only use columns A and B, and you will not rely on any other columns that may be present in the data source. However, if you are liberal in what you accept from others, you will be open to accepting additional columns that may be present in the data source, as long as they do not interfere with your use of columns A and B. This can help to ensure that your project is robust and can handle changes in the data source without breaking as long as the critical columns A and B are still present and functioning properly!


10. Scope Handshake Principle (Created by me!)

    This principle states that when two or more people are working on a project, they need to have a clear understanding of the scope of their work and how it fits into the overall project. This can be achieved through a "handshake" where each person communicates their understanding of the scope and how it relates to the work of others. This can help to ensure that everyone is on the same page and that there are no misunderstandings or miscommunications that can lead to delays or issues in the project. By following this principle, teams can work more efficiently and effectively, and can avoid potential conflicts or issues that may arise from a lack of clarity around the scope of work! 

    Suppose you have a certain job that needs to be executed in Databricks. However, the team that is accountable for deploying the job in the production environment expects the job to be executed from Azure Synapse, so basically: `Azure Synapse --> Databricks`. Also, the Azure Synapse piece is handled by another team. If there is no clear understanding of the scope of work and how it relates to the overall project, it can lead to a lot of confusion and miscommunication between the teams, which can ultimately lead to delays and issues in the project. However, a simple principle can be established as follows:

    * Team 1, who is accountable for developing the job in Databricks, is responsible for developing the job and making sure that it can be executed in Databricks. They are not responsible for how the job will be executed from Azure Synapse, as long as it can be executed in Databricks without any issues. 

    * Team 1 needs to communicate and share:
        - The code that they have developed in Databricks
        - The parameters that they are using in Databricks
        - The expected output of the job in Databricks
        - The compute resources that they are using in Databricks

    * Team 2 can collect the information from Team 1 and use it to execute the job from Azure Synapse. They are responsible for making sure that the job can be executed from Azure Synapse without any issues, as long as it can be executed in Databricks without any issues.

    * Team 2 can then communicate and share:
        - The code that they have developed in Azure Synapse to execute the job in Databricks
        - The parameters that they are using in Azure Synapse to execute the job in Databricks
        - The expected output of the job when executed from Azure Synapse
        - The compute resources that they are using in Azure Synapse to execute the job in Databricks

    * Team 3 can then collect the information from Team 2 and use it to deploy the job in the production environment. They are responsible for making sure that the job can be deployed in the production environment without any issues, as long as it can be executed from Azure Synapse without any issues.


