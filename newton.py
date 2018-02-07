from math import *
from numpy import *
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

def f_string():
    fn_string = "pow(x,3)-x-exp(x)-1"
    return fn_string

def f(x):
    #tmp = 1.2*pow(x,3)+2*pow(x,2)-20*x-10
    #tmp = x - 2.0*exp(-x)
    string = f_string()
    tmp = eval(string)
    return tmp

def fprime(x):
    tmp = 3*pow(x,2)-1-exp(x)
    return tmp


#Newton Raphson
#this is an Open method...

x_root = [3.3]

max_iterations = 100
count = 0
#xns = [(a*f(b)-b*f(a))/(f(b)-f(a))]
err_stop = 0.001
relerr=[1.1*err_stop]

while relerr[count] > err_stop and count < max_iterations:
    count +=  1
    tmp = x_root[count-1]-f(x_root[count-1])/fprime(x_root[count-1])
    x_root.append(tmp)
    tmp = abs((x_root[count] - x_root[count - 1]) / x_root[count])
    relerr.append(tmp)
    print x_root[count], relerr[count]

relerr.pop(0)
x_start = min(x_root)
x_end = max(x_root)
x = np.linspace(x_start,x_end,100)

function_name = f_string()
title_base = "Plot of " + function_name
title = title_base
filename = "Newton_method_"+function_name+".png"
xlabel = "x"
ylabel = "f(x)"
root_data_label = "root approximations"
y_func_label = function_name

FunctionRootPlot111(x,xlabel,f,ylabel,x_root,root_data_label,title,filename)









