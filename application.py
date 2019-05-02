import re
from github import *
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

def get_total_seconds(issue_timestamp):
	'''
	Returns the difference in issue's timestamp and system's timestamp (current time)
	'''
	time_delta = datetime.now().timestamp() - issue_timestamp
	return time_delta

def get_repo_stats(repo_name):
	'''
	Returns a dictionary containing the respective count of issues
	'''

	# Creating a Github instance using Access Token
	g = Github()

	# Get the repository
	repo = g.get_repo(repo_name)

	# Get all the open issues from the repository
	open_pulls = repo.get_pulls(state='open')
	open_pull_titles = [pull.title for pull in open_pulls]
	open_issues = repo.get_issues(state='open')
	open_issues = [issue for issue in open_issues if issue.title not in open_pull_titles]
	print(len(open_issues))

	# Create a dictionary ('keys' are the desired strings, 'values' are the count of issues)
	stats_dict = {'Total Open Issues':len(open_issues),
	'Opened in last 24 hours':0,
	'Opened more than 24 hours ago but less than 7 days ago':0,
	'Opened more than 7 days ago':0}

	# Populate the dictionary
	for issue in open_issues:
		created_at = issue.created_at.timestamp()
		delta = get_total_seconds(created_at)
		if delta <= 86400:
			stats_dict['Opened in last 24 hours'] += 1
		elif delta > 86400 and delta <= 604800:
			stats_dict['Opened more than 24 hours ago but less than 7 days ago'] += 1
		elif delta > 604800:
			stats_dict['Opened more than 7 days ago'] += 1
	return stats_dict

# Create a Flask application object
app = Flask(__name__)

# This decorator is used to display the home page when blank URL ('/') is loaded
@app.route('/', methods=['POST', 'GET'])
def index():
	repo_name = ''
	stats_dict = ''
	if request.method == 'POST' and request.form['repo_name']:
		repo_name = request.form['repo_name']
		repo_name = re.search('github.com/(.*)', repo_name).group(1)
		stats_dict = get_repo_stats(repo_name)
	'''
	home.html is loaded when blank URL is loaded. It displays the input field for repo name and a button.
	If the button is clicked after entering the repository name, repo_name and stats_dict arguments will be 
	populated and home.html will be loaded again which will display the table of issue counts.
	'''
	return render_template('home.html', repo_name=repo_name, stats_dict=stats_dict)


if __name__ == '__main__':
	app.run(debug=True)