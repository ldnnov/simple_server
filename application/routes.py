from flask import render_template, redirect, url_for
from flask import current_app as app, jsonify, request
from .models import db, Counter


@app.route('/')
def index():
    content_type = request.headers.get('Content-Type')
    counter = Counter.query.first()

    if content_type == 'application/json':
        data = jsonify(counter=counter.value)
    else:
        data = render_template('index.html', counter=counter.value)

    counter.value += 1
    db.session.commit()

    return data


@app.route('/reset')
def reset_counter():
    counter = Counter.query.first()
    counter.value = 0
    db.session.commit()

    return redirect(url_for('index'))
