# !/usr/bin/env python3
# coding: utf-8
""" index.py """

from pathlib import Path
from bottle import route, post, run, default_app, error, request
from bottle import TEMPLATE_PATH as template_path, jinja2_template as template
from bottle import static_file

base = Path(__file__).parent
template_path.append(base / 'views')


@route('/<filepath:path>')
def static_files(filepath):
    return static_file(Path(filepath).name, root=base / "assets" / Path(filepath).parent)


@route('/')
def index():
    """ index page """
    return template('index')


@post('/')
def post_index():
    """ post index """
    input_value = request.forms.input_value

    if input_value == "info":
        return template('index', info=input_value)
    elif input_value == "warn":
        return template('index', warn=input_value)
    else:
        return template('index', error=input_value)


@error(404)
def error404(ex):
    """ file not found error """
    return "error 404 : {0}".format(ex.body)


@error(500)
def error500(ex):
    """ internal server error """
    return "error 500 : {0}".format(ex.args[2])


if __name__ == '__main__':
    run(host='localhost', port=3030)
else:
    application = default_app()
