#Keshav Bimbraw

import numpy as np

#-------------------------------------------------------------
#First function
#decimate_by_2 function taking in input x
def decimate_by_2(x):
    
    #initializing output array index
    j = 0

    #to 'keep' first value
    x = np.append(0,x)
    
    #for all values to be float
    x = map(float, x)


    #different cases defined for lossless decimation
    #Even length case
    if len(x)/2 == 0:
        out = np.zeros(((len(x)-1)/2))
        for i in range(0,len(x)):
            if i % 2 != 0:
                out[j] = x[i]
                j = j+1
                
    #odd length case
    else:
        out = np.zeros((len(x)/2))
        for i in range(0,(len(x))):
            if i % 2 != 0:
                out[j] = x[i]
                j = j+1
    
    print(out)
    return out


#-------------------------------------------------------------
#Second function
#downsample_by_2 convolving Kaiser filter coefficients with input
def downsample_by_2(x):
    
    #reading file
    with open('kaiser_filter_32.txt', 'r') as my_file:
        text = my_file.read()
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("\n", "")
    
    h = list(text.split(','))
    
    #converting both to float
    h = map(float, h)
    x = map(float, x)

    #using numpy's convolve (numpy.convolve) with Mode specified
    #as 'same'. Mode ‘same’ returns output of length max(M, N)
    y = np.convolve(x,h,'same')

    #multiplying by 2 to account for downsampling
    y = y * 2
    
    #Using decimate_by_2 function implemented above
    decimate_by_2(y)

#defining an arbitrary input signal to test the output
input_signal = [1,2,3,4,5,-6]
downsample_by_2(input_signal)


#-------------------------------------------------------------
#Bonus implementation
#-------------------------------------------------------------
#Bonus - own implementation of general convolution
def own_implementation_general_convolution(x):
    
    #reading file
    with open('kaiser_filter_32.txt', 'r') as my_file:
        text = my_file.read()
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("\n", "")
    
    h = list(text.split(','))
    
    #converting to float
    h = map(float, h)
    x = map(float, x)
    
    #length of output
    length_val = len(x)+len(h)-1

    #initializing output array
    out_own = np.zeros(length_val)
    
    #append by zeros
    append_vals_x = np.zeros(len(h)-1)
    append_vals_h = np.zeros(len(x)-1)
    x = np.append(x,append_vals_x)
    h = np.append(h,append_vals_h)

    #heart of the code - discrete 1D convolution operation
    for i in range(0,length_val):
        out_own[i] = 0
        for j in range(0,i+1):
            out_own[i] = out_own[i] + (x[j]*h[i-j])
    
    #returning the output
    return out_own

#My own implementation of general convolution operation
#UNCOMMENT TO SEE THE OUTPUT
#own_implementation_general_convolution(input_signal)