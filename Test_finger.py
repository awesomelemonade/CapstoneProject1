import numpy as np
def peaks_to_fingerprints(peaks, fanout):
    times,freqs = np.where(peaks.T)#gets data
    print(freqs, times)
    fanout_ = np.arange(fanout) + 1#makes an array for all the differences of indexes (ie f1 f2 to f1 f16 or something)
    frequency_index = np.arange(len(freqs)) #makes an array for every index in data(i: 0,1,2,3,4,5,6)
    index_chart = frequency_index.reshape(-1,1) + fanout_ #makes a chart of all the indexes, row = f2 values associated with f1 (col)
    index_chart[index_chart >= len(frequency_index)] = len(frequency_index) - 1 #min(last index, index produced)
    data_chart = freqs[index_chart]#advance index on data to create frequencies
    ones = np.ones(fanout) #makes rows of ones (used later)
    data_stretched = (freqs.reshape(-1,1) * ones).flatten() #makes an array thats the same shape as data_chart, then flatten it so you can later vstack them
    time_chart = times[index_chart] #ditto for time
    time_stretch = (times.reshape(-1,1) * ones)
    time_diff = time_chart - time_stretch
    print(np.shape(data_stretched))
    print(np.shape(data_chart))
    print(np.shape(time_diff))
    print(np.shape(time_stretch))
    final_data = np.vstack([data_stretched, data_chart.flatten(), time_diff.flatten(), time_stretch.flatten()]).T #vstacks all data
    return final_data[:-1]
