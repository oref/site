import sys
import webbrowser
from flask import Flask, render_template
from flask_flatpages import FlatPages

FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/projects')
def projects():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
