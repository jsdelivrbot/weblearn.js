from __future__ import division
def mean(x):
    return sum(x)/len(x)
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    if n%2==1
        return sorted_v[midpoint]
    else:
        lo = midpoint-1
        hi = midpoint
        return (sorted_v[lo]+sorted_v[hi])/2