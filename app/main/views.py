from flask import render_template
from . import main
import os

@main.route('/')
def index():
    fs = os.listdir('./app/templates')
    print fs
    """Render website's home page."""
    return render_template('index.html')


@main.route('/notebooks/<path:loc>')
def home(loc):
    print loc
    """Render website's home page."""
    return render_template(loc)






