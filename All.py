#%% Sampling std
import numpy as np
n = 100
std=5.6
sampling_std=std/np.sqrt(n)
#%%
#Tüm olası örneklem ortalamasının (Ẋ) %68’i ±1 z skor aralığındadır.

#Tüm olası örneklem ortalamasının (Ẋ) %95’i ±2 z skor aralığındadır.

#Tüm olası örneklem ortalamasının (Ẋ) %99’u ±3 z skor aralığındadır.
# confidence interval two tailed z test
from scipy.stats import norm
# define probability
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)
x=np.array([5,10,15,20])
mean=60000
std=3000
# confirm with cdf
# populasyon std biliniyor ve n>100
upper_conf_interval = mean +value * (std/np.sqrt(len(x)))
lower_conf_interval = mean -value * (std/np.sqrt(len(x)))
print(lower_conf_interval,upper_conf_interval)
#%% populasyon std bilinmiyor ve n>100
upper_conf_interval = mean +value * (std/np.sqrt(len(x)-1))
lower_conf_interval = mean -value * (std/np.sqrt(len(x)-1))
print(lower_conf_interval,upper_conf_interval)
#%% confidence z interval for proportion
from scipy.stats import norm
# define probability
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)
count = 60
total = 200
ps = count/total
ps = 0.4
pu = 0.5
upper_conf_interval = ps +value * (np.sqrt((pu*(1-pu))/len(x)))
lower_conf_interval = ps -value * (np.sqrt((pu*(1-pu))/len(x)))
print(lower_conf_interval,upper_conf_interval)
#%% Ortalamanın Two tailed hypotesis testing
#H0 mean = aranan_ort
#H1 mean != aranan_ort
# define probability
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)
mean = 60000
std= 3000
N= 1200
aranan_ort = 25000
z = (aranan_ort - mean) /(std/np.sqrt(N))
if (z > value) | (z< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% Ortalamanın One tailed  hypotesis testing
#H0 mean => aranan_ort
#H1 mean < aranan_ort   
p = 0.95 
# retrieve value <= probability
value = norm.ppf(p)
print(value)
mean = 4
std= 1.2
N= 120
aranan_ort = 4.5
z = (aranan_ort - mean) /(std/np.sqrt(N))
if (z > value) | (z< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% Two tailed hypotesis testing for proportion
#H0 ps = pu
#H1 ps != pu
count = 53
total = 122
ps = count/total
pu = 0.39
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)

z = (ps -pu)/np.sqrt((pu*(1-pu)/total))
if (z > value) | (z< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% 
#%% Ortalamanın tek örneklem testi n<=30
#%%Serbestlik derecesi = N1 - 1
#H0 mean = aranan_ort
#H1 mean != aranan_ort
value = 2.756
mean=2.5
aranan_ort = 2.78
std=1.23
n=30
t=(aranan_ort-mean)/(std/(np.sqrt(n-1)))
if (t > value) | (t< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% Ortalamanın İki örneklem testi büyük örneklem > 30
#H0 mean1 = mean2
#H1 mean1 != mean2
mean_1=2.37
mean2=2.78
std_1=0.63
std_2=0.95
n1=42
n2=37
std_birlesik = np.sqrt((std_1**2)/(n1-1)+((std_2**2)/(n2-1)))
z = (mean_1 - mean2)/std_birlesik
# define probability
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)
if (z > value) | (z< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% Ortalamanın İki örneklem testi büyük örneklem <= 30
#H0 mean1 = mean2
#H1 mean1 != mean2    
#Serbestlik derecesi = N1 + N2 - 2
value = -2.28
mean_1=2.37
mean2=2.78
std_1=0.63
std_2=0.95
n1=42
n2=37
std_birlesik = np.sqrt(((n1*std_1**2)+(n2*std_2**2))/(n1+n2-2)) * np.sqrt((n1+n2)/(n1*n2))
t = (mean_1 - mean2)/std_birlesik
if (t > value) | (t< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")
#%% Orantı İçin iki örneklem Hipotez Testi n>30
count1 = 53
total1 = 83
ps1 = count1/total1
ps1 = 0.34
count2 = 53
total2 = 103
ps2 = count2/total2
ps2=0.25
p = 0.975 
# retrieve value <= probability
value = norm.ppf(p)
print(value)

pu_toplam = ((total1*ps1) + (total2*ps2))/(total1+total2)
std_p_p = np.sqrt(pu_toplam*(1-pu_toplam)) * np.sqrt((n1 + n2)/(n1*n2))
z = (ps1-ps2) / std_p_p
if (t > value) | (t< -value):
    print("H0 reddedildi")
else:
    print("H0 red edilemedi")











