peaks = np.array([[True, False, False],
                  [False, True, False],
                  [True, True, False]])
def peaks_to_fingerprints(peaks, fanout):
    times,freqs = np.where(peaks.T)#gets data
    fanout_ = np.arange(fanout) + 1#makes an array for all the differences of indexes (ie f1 f2 to f1 f16 or something)
    frequency_index = np.arange(len(freqs)) #makes an array for every index in data(i: 0,1,2,3,4,5,6)
    index_chart = (frequency_index.reshape(-1,1) + fanout_).flatten() #makes a chart of all the indexes, row = f2 values associated with f1 (col)
    index_chart = index_chart[index_chart < len(frequency_index)] #min(last index, index produced)
    data_chart = freqs[index_chart]#advance index on data to create frequencies
    ones = np.ones(fanout) #makes rows of ones (used later)
    data_stretched = (freqs.reshape(-1,1) * ones).flatten()[:len(index_chart)] #makes an array thats the same shape as data_chart, then flatten it so you can later vstack them
    time_chart = times[index_chart].flatten() #ditto for time
    time_stretch = (times.reshape(-1,1) * ones).flatten()[:len(index_chart)]
    time_diff = time_chart - time_stretch
    final_data = np.vstack([data_stretched, data_chart, time_diff, time_stretch]).T #vstacks all data
    return tuple(map(tuple, final_data))

peaks_to_fingerprints(peaks, 4)




