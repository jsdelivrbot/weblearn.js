from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
app = Flask(__name__)

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

from Functions import LinearAlgebra as linAlg

import json


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, list):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route("/", methods=['GET','POST','OPTIONS'])
@crossdomain(origin="*")
def run():
	parameters = request.form['params']
	function = request.form['function']
	#print (parameters)
	if(function=="vector_add()"):
		closeInd = parameters.index("]")
		openInd = parameters.index("[",2)
		v1str = parameters[1:closeInd]
		v2str = parameters[(openInd+1):(len(parameters)-1)]
		v1 = [int(s) for s in v1str.split(',')]
		v2 = [int(s) for s in v2str.split(',')]
		print (v1)
		print (v2)
		result = linAlg.vector_add(v1,v2)
	return ''.join(str(e) for e in result)



if __name__ == '__main__':
    app.run()