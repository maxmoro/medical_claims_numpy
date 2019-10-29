"""
https://realpython.com/numpy-array-programming/

"""


#%% Init
import numpy as np
import os
import sys

#%% Read file

#data=np.genfromtxt("claim.sample.csv",dtype='str',skip_header=1)
# https://stackoverflow.com/questions/23319266/using-numpy-genfromtxt-gives-typeerror-cant-convert-bytes-object-to-str-impl
data=np.genfromtxt("claim.sample.csv",delimiter=',',dtype='f8')
