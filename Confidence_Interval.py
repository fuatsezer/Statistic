#%% Confidence Interval for the Population Mean
import numpy as np
import scipy.stats
def mean_confidence_interval(x, confidence=0.95):
    a = 1.0 * np.array(x)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h
a = range(10,14)
print(mean_confidence_interval(a))
#%% Confidence Interval for Proportions
from statsmodels.stats.proportion import proportion_confint
print(proportion_confint(count=310,    # Number of "successes"
                   nobs=1126,    # Number of trials
                   alpha=(1 - 0.95)))
#%% Confidence Interval for the Population Variance
from scipy import stats
import numpy as np
arr = [8.69, 8.15, 9.25, 9.45, 8.96, 8.65, 8.43, 8.79, 8.63]
alpha = 0.05               # significance level = 5%
n = len(arr)               # sample sizes
s2 = np.var(arr, ddof=1)   # sample variance
df = n - 1                 # degrees of freedom
upper = (n - 1) * s2 / stats.chi2.ppf(alpha / 2, df)
lower = (n - 1) * s2 / stats.chi2.ppf(1 - alpha / 2, df)
print((lower, upper))



