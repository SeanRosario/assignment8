__author__ = 'SeansMBP'
from Question2 import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys

def simulation():


    positions= [1,10,100,100]
    num_trials = 10000
    results = open("results.txt","w")


    for p in positions:
        daily_ret_list= the_trials(num_trials,p)
        daily_ret = dict_to_list(daily_ret_list)
        print daily_ret
        #doing the plotting

        plt.hist(daily_ret,100,range=[-1,1])
        plt.savefig("histogram_{0}_pos.pdf".format(str(p).zfill(4)))
        #plt.show()
        plt.clf()
        plt.close()

        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        results.write("The mean for position {0} is {1} and it Std. deviation is {2} \n".format(p,mean,std))





def dict_to_list(a_dict):
    a_list= []
    for i in range(len(a_dict)):
        temp = a_dict[i]
        a_list.append(temp)
    return a_list
