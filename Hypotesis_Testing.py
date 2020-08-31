#%% UNIVARIATE TESTS FOR NORMALITY
from scipy import stats
x = np.linspace(-15, 15, 9)
print(stats.kstest(x, 'norm'))
#%% Shapiro-wilks test 4<=n<=2000
from scipy import stats
x = stats.norm.rvs(loc=5, scale=3, size=100)
print(stats.shapiro(x))
#%% Shapiro-Francia Test 5<=n<=5000
#%% TESTS FOR THE HOMOGENEITY OF VARIANCES - Levene F test
# H0: the population variances of all three groups are homogeneous
# H1: the population variance of at least one group is different from the others
from scipy import stats
x = stats.norm.rvs(loc=5, scale=3, size=100)
x2 = stats.norm.rvs(loc=7, scale=3, size=100)
print(stats.levene(x,x2))
#%% Levene ttest >=0.05 ve shapiro >= 0.05 One-way ANOVA
#%% Nonparametric Tests
#Before After Wilcoxon test
from scipy import stats
print(stats.wilcoxon(x,x2))
#%% Independent whitney u test
# H0: m1 = m2
# H1: m1 != m2
from scipy import stats
print(stats.mannwhitneyu(x,x2))
#%% Paired more than 2 Friedman's test
# H0: m1 = m2 =...= mk
x = stats.norm.rvs(loc=5, scale=3, size=100)
x2 = stats.norm.rvs(loc=7, scale=3, size=100)
x3 = stats.norm.rvs(loc=8, scale=3, size=100)

from scipy import stats
print(stats.friedmanchisquare(x,x2,x3))
#%% Independent more than 2 Kruskal test
from scipy import stats
print(stats.kruskal(x,x2,x3))
#%% hypotesis test for proportions
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
count = np.array([5, 12])
nobs = np.array([83, 99])
stat, pval = proportions_ztest(count, nobs)
print('{0:0.3f}'.format(pval))
#%% One-Tail Hypothesis Tests
values = np.random.normal(loc=0, scale=10, size=6000)
two_std_from_mean = np.mean(values) + np.std(values)*1.645
kde = stats.gaussian_kde(values)
pos = np.linspace(np.min(values), np.max(values), 10000)
plt.plot(pos, kde(pos), color='teal')
shade = np.linspace(two_std_from_mean, 40, 300)
plt.fill_between(shade, kde(shade), alpha=0.45, color='teal')
plt.title("Sampling Distribution for One-Tail Hypothesis Test", y=1.015, fontsize=20)
plt.xlabel("sample mean value", labelpad=14)
plt.ylabel("frequency of occurence", labelpad=14);
print(two_std_from_mean)
#%% Two-Tailed Hypothesis Tests
values = np.random.normal(loc=0, scale=10, size=6000)
alpha_05_positive = np.mean(values) + np.std(values)*1.96
alpha_05_negative = np.mean(values) - np.std(values)*1.96
kde = stats.gaussian_kde(values)
pos = np.linspace(np.min(values), np.max(values), 10000)
plt.plot(pos, kde(pos), color='dodgerblue')
shade = np.linspace(alpha_05_positive, 40, 300)
plt.fill_between(shade, kde(shade), alpha=0.45, color='dodgerblue')
shade2 = np.linspace(alpha_05_negative, -40, 300)
plt.fill_between(shade2, kde(shade2), alpha=0.45, color='dodgerblue')
plt.title("Sampling Distribution for Two-Tail Hypothesis Test", y=1.015, fontsize=20)
plt.xlabel("sample mean value", labelpad=14)
plt.ylabel("frequency of occurence", labelpad=14);
print(alpha_05_negative,alpha_05_positive)
#%%
