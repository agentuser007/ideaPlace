# ideaPlace

IdeaPlace is a cloud-based web application that allows users to create, explore, and collaborate on ideas. The application is built using Django, Python, and SQLite3, with the frontend designed using HTML and Bootstrap. It is deployed on AWS Elastic Beanstalk, utilizing AWS CodeBuild and AWS CodeDeploy for continuous integration and deployment.

## Features

- User registration and authentication
- Idea creation, updating, and deletion
- Displaying a list of all ideas on the homepage
- Detailed view of individual ideas on separate pages
- Recommendation system for top ideas based on likes
- Search functionality for ideas based on title or content
- Ability to post ideas with images
- User profile pages displaying liked ideas and the ability to edit and delete their own ideas

## Architecture

IdeaPlace follows a monolithic architecture, with the backend server built using Python and Django, and the frontend designed using HTML and Bootstrap. The database is managed using SQLite3. The application is deployed on AWS Elastic Beanstalk, which provides scalability and reliability.

## Library

A custom library has been developed for IdeaPlace, providing utility functions for text manipulation and idea ranking.


## Deployment

IdeaPlace is deployed on AWS Elastic Beanstalk. Continuous integration and deployment in AWS CodePipeline are achieved using AWS CodeBuild and AWS CodeDeploy.
