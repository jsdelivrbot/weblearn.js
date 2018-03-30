import math
def vector_add(params):
    return [v_i + w_i
            for v_i, w_i in zip(params[0],params[1])]
def vector_subtract(params):
    return [v_i-w_i
            for v_i, w_i in zip(params[0],params[1])]
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add([result, vector])
    return result
def scalar_multiply(c,v):
    return [c*v_i for v_i in v]
def vector_mean(vector):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
def dot(v,w):
    return sum(v_i*w_i
                for v_i, w_i in zip(v,w))
def sum_of_squares(v):
    return dot(v,v)
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))
def distance(v,w):
    return math.sqrt(squared_distance(v,w))
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows,num_cols
def get_row(A, i):
    return A[i]
def get_column(A, j):
    return [A_i[j]
            for A_i in A]
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
            for j in range(num_cols)]
            for i in range(num_rows)]
