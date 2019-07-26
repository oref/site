import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', pages=pages)


@app.route('/<path:path>/')
def page(path):
    page_ = pages.get_or_404(path)
    return render_template('page.html', page=page_)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True, host='0.0.0.0')
