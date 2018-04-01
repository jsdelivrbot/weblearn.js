from matplotlib import pyplot as plt
import random
def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0
def uniform_cdf(x):
    if x<0: return 0
    elif x<1: return x
    else: return 1
def normal_pdf(x,mu=0,sigma=1):
    sqrt_two_pi = math.sqrt(2*math.pi)
    return (matah.exp(-(x-mu)**2/2/sigma**2)/sqrt_two_pi*sigma)
def normal_cdf(x):
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2
def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    if mu!=0 or sigma !=1:
        return mu+sigma*inverse_normal_cdf(p,tolerance=tolerance)
    low_z = -10.0
    hi_z = 10.0
    while hi_z -low_z > tolerance:
        mid_z = (low_z+hi_z)/2
        mid_p=normal_cdf(mid_z)
        if mid_p < p:
            low_z=mid_z
        elif mid_p > p:
            hi_z=mid_z
        else:
            break
    return mid_z
def bernoulli_trial(p):
    return 1 if random.random() < p else 0
def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))
def make_hist(p,n,num_points):
    data = [binomial(n,p) for _ in range(num_points)]
    histogram = Counter(data)
    plot.bar([x-0.4 for x in histogram.keys()],
    [v/num_points for v in histogram.values()],
    0.8,
    color='0.75')
    mu = p*normal_cdfsigma = math.sqrt(n*p*(1-p))
    xs = range(min(Data), max(data) + 1)
    ys = [normal_cdf(i+0.5,mu,sigma) - normal_cdf(i-0.5,mu,sigma)
            for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal APproximation")
    plt.show()