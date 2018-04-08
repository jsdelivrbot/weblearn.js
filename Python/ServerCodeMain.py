from __future__ import division
#NOTHING BEFORE THIS>> ALL IMPORTS BELOW

#sklearn imports
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

import numpy as np
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
app = Flask(__name__)
#import sklearn

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

import random

import json

params = " "
result = " "

import math

######## Linear Algebra ############
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

#make matrix - func in param tries to eval in exec, so don't use
def make_matrix(params):
    num_rows=params[0]
    num_cols=params[1]
    entry_fun=params[2]
    return [[entry_fn(i,j)
        for j in range(num_cols)]
            for i in range(num_rows)]
#useless
def is_diagonal(i,j):
	return 1 if i==j else 0
######### Stat #########################
def mean(x):
    return sum(x)/len(x)
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    if n%2==1:
        return sorted_v[midpoint]
    else:
        lo = midpoint-1
        hi = midpoint
        return (sorted_v[lo]+sorted_v[hi])/2
def quantile(params):
    x=params[0]
    p=params[1]
    p_index = int(p*len(x))
    return sorted(x)[p_index]
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return[x_i for x_i, count in counts.iteriterms()
            if count == max_count]
def data_range(x):
    return max(x)-min(x)
def de_mean(x):
    x_bar = mean(x)
    return [x_i -x_bar for x_i in x]
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)
def standard_deviation(x):
    return math.sqrt(variance(x))
def interquartile_range(x):
    return quantile(x,0.75)-quantile(x,0.25)
def covariance(params):
    x=params[0]
    y=params[1]
    n = len(x)
    return dot(de_mean(x),de_mean(y))/(n-1)
def correlation(params):
    x = params[0]
    y = params[1]
    stdev_x=standard_deviation(x)
    stdev_y=standard_deviation(y)
    if stdev_x>0 and stdev_y>0:
        return covariance([x,y])/stdev_x / stdev_y
    else:
        return 0

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(params):
    n = params[0]
    p = params[1]
    return sum(bernoulli_trial(p) for _ in range(n))

### Don't use make hist
def make_hist(params):
    p = params[0]
    n = params[1]
    num_points = params[2]
    data = [binomial([n,p]) for _ in range(num_points)]
    histogram = Counter(data)
    plot.bar([x-0.4 for x in histogram.keys()],
    [v/num_points for v in histogram.values()],
    0.8,
    color='0.75')
    mu = p*normal_cdf
    sigma = math.sqrt(n*p*(1-p))
    xs = range(min(Data), max(data) + 1)
    ys = [normal_cdf(i+0.5,mu,sigma) - normal_cdf(i-0.5,mu,sigma)
            for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal APproximation")
    plt.show()



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


################################################# SKLEARN FULL MODELS ###################
def linear_regression(params):
	x = np.asarray(params[0])
	y = np.asarray(params[1])
	predictXVal = params[2]
	model = LinearRegression()
	model.fit(x,y)
	predictedYVal = model.predict(predictXVal)
	return predictedYVal

def support_vector_machine(params):
	x = params[0]
	y = params[1]
	predict = params[2]
	clf = SVC()
	clf.fit(x, y)
	return(clf.predict([predict]))
def neural_network(params):
    x = params[0]
    y = params[1]
    predict = params[2]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, 
                            hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x, y)
    return clf.predict(predict)

####################################### SERVER LOGISTICS #################################

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