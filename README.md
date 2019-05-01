# GitHub Repository Stats Reader

This is a Flask app to manage the GitHub resources like repositories, user profiles, and organizations.
Currently this app is limited to fetch the statistics related to open issues of any public GitHub repository.

This app takes the repository link (https://github.com/repository-name) as input and displays the following:

- Total number of open issues
- Number of open issues that were opened in last 24 hours
- Number of open issues that were opened more than 24 hours ago but less than 7 days ago
- Number of open issues that were opened more than 7 days ago

#### Technologies used:
The app is written completely in Python.
- PyGithub: This is a Python library to access the GitHub APIs. This library enables us to manage GitHub resources such as repositories, user profiles, and organization in our Python applications.
- Flask: This is a micro framework for Python web applications.

#### Solution:
The repository name entered by the user is read and used to fetch the statistics of open issues.
In statistics, we get issue titles, created_at date, comments, issue_id, updated_at date, state etc...
I have used created_at date of an issue and calculated the total number of seconds from current system time.
For a particular issue, if the total_seconds are less than 86400 (which means 24 hours), then I add this issue to corresponding count. Similarly I count the other issues which were opened more than 24 hours ago and less than 7 days ago.
Also for the issues which were opened more than 7 days ago.
I create a dictionary and pass it to the html template where these are displayed in tabular form.

#### Deployment:
I have used AWS elastic beanstalk. AWS_EB is an orchestration service offered from Amazon Web Services for deploying your application .
The live app can accessed [here](http://git-repo-stats.iezddgdcd9.us-east-2.elasticbeanstalk.com/).

#### Areas of improvements:
This app can further be developed to perform more sophisticated tasks.
A user should be able to manager her GitHub account using this app.
Apart from fetching statistics, this app can also be used to edit the repositories and user information.
Just like we fetched the open issues, we can open new issues and add comments to existing issues using this app.
