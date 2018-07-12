def dig_to_spec(data, fs):
    return mlab.specgram(data, NFFT=4096, Fs=fs,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)
                            

def spec_to_peaks(data, value, fp = generate_binary_structure(rank = 2, connectivity=2)):
    max_arr = maximum_filter(data, footprint = fp)
    return (arr == max_arr) & (arr > value)
