import os

from data import db_session
from flask import Flask, render_template, url_for
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    base_params = {'css_path': url_for('static', filename='css/style.css')}
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', title='Works log', jobs=jobs, **base_params)


if __name__ == '__main__':
    db_session.global_init(os.path.join('db', 'mars_explorer.db'))
    app.run()