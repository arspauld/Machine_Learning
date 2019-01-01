#ludicrous number of imports
import numpy
import h5py
import os

#declare a list to contain CY data
CY = []

#import the first file
#CY.append(h5py.File('../../sram flash data/sram/CY_1_HTHV_fresh_50_trials.mat', 'r'))
file_list = os.listdir('../../sram flash data/sram/')

#import all CY.mat files
for i in file_list:
    if i.endswith('.mat') and i.startswith('CY'):
        data = h5py.File('../../sram flash data/sram/'+i, 'r')
        data = numpy.array(data.get('data'))
        CY.append(data.flatten())

#test prints for CY.mat files
print(CY[0])


#normalizing function
def __sigmoid(x):
    return 1/(1+numpy.exp(-x))

#derivative to calculate gradient vector
def __sigmoid_derivative(x):
    return (1/(1+numpy.exp(-x)))-((1/(1+numpy.exp(-x)))**2)

