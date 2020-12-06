from flask import json
from flask import Response
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/summary')
def summary():
    data = {'firstname': 'José', 'lastname': 'Jiménez'}

    return Response(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
