#!/usr/bin/python3
""" Flask web app
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """ tear down app context on end """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ list states from database
    return HTML
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
