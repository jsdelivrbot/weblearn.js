from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
app = Flask(__name__)

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

from Functions import LinearAlgebra as linAlg

import json

params = " "
result = " "

import math
def vector_add(params):
    return [v_i + w_i
            for v_i, w_i in zip(params[0],params[1])]
def vector_subtract(v,w):
    return [v_i-w_i
            for v_i, w_i in zip(params[0],params[1])]
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add([result, vector])
    return result
def scalar_multiply(params):
    return [params[0]*v_i for v_i in params[1]]
def vector_mean(vector):
    n = len(vectors)
    return scalar_multiply([1/n, vector_sum(vectors)])
def dot(params):
    return sum(v_i*w_i
                for v_i, w_i in zip(params[0],params[1]))
def sum_of_squares(v):
    return dot([v,v])
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
def squared_distance(params):
    return sum_of_squares(vector_subtract(params[0],params[1]))
def distance(params):
    return math.sqrt(squared_distance([params[0],params[1]]))
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows,num_cols
def get_row(params):
    A = params[0]
    i = params[1]
    return A[i]
def get_column(params):
    A = params[0]
    i = params[1]
    return [A_i[j]
        for A_i in A]
def make_matrix(params):
    num_rows=params[0]
    num_cols=params[1]
    entry_fun=params[2]
    return [[entry_fn(i,j)
        for j in range(num_cols)]
            for i in range(num_rows)]

def is_diagonal(i,j):
	return 1 if i==j else 0


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
	paramsRawVal = request.form['params']
	function = request.form['function']
	parametersexec = "global params; params=" + paramsRawVal
	exec(parametersexec)
	resultRawCode = "global result; result=" + function + "(" + paramsRawVal + ")"
	print(resultRawCode)
	exec(resultRawCode)
	global result
	if(result != " "):
		print(result)
	else:
		result = "an error occurred or no value was returned"
	return ','.join(str(e) for e in result)



if __name__ == '__main__':
    app.run()