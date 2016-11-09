from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}  # fake user
	
	posts = [
		{
			'author':{'nickname':'AllynH'},
			'body':'Beautiful day in Maynooth!'
		},
		{
			'author':{'nickname':'Susan'},
			'body':'The Avengers movie was so cool!'
		}
	]
	
	return render_template (
		'index.html',
		title='Home',
		user=user,
		posts=posts
		)
