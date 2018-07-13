# imports
import databasing
import numpy as np

""" Intakes a 2D array of peaks and returns a List containing keys and times.

        This takes in input from the function spectrogram_to_peaks()
        and returns output that can be used as a dictionary key in
        the song database.

        Parameters
        ----------
        peaks : numpy.ndarray
        fanout : int

        Returns
        -------
        List
            Returns a list with length N, where N is the number of
            peaks. Each element has a tuple containing the keys,
            which are type Tuple, and the time bins, which are type
            int. The keys are formatted as (f1, f2, t2-t1)."""
def peaks_to_fingerprints(peaks, fanout):
    # gets two arrays, frequency and time. Use np.where on peaks
    times, freqs = np.where(peaks.T)

    # this was like 90% edison so creds to him
    frequency_index = np.arange(len(freqs)) # makes an array for every index in data(i: 0,1,2,3,4,5,6)
    index_chart = (frequency_index.reshape(-1,1) + (np.arange(fanout) + 1)).flatten() # makes a chart of all the indexes, row = f2 values associated with f1 (col)
    index_chart2 = index_chart[index_chart < len(frequency_index)] # deletes indicies that don't exist
    index_chart[index_chart >= len(frequency_index)] = -1 #reusing index chart to get out of bounds to be negative

    ones = np.ones(fanout)
    f1 = (freqs.reshape(-1,1) * ones).flatten()[index_chart >= 0] # frequency 1
    f2 = freqs[index_chart2].flatten() # frequency 2
    t1 = (times.reshape(-1,1) * ones).flatten()[index_chart >= 0] # time 1
    delta_t = (times[index_chart2].flatten() - t1) # change between time 2 and time 1
    # creds to anna
    key_times = np.vstack((f1, f2, delta_t, t1)).T.astype(int)
    # key_times = list(tuple(zip(map(tuple, key_times[:, :3]), key_times[:, 3]))) # had to get rid of the named tuple for formatting, to be fixed
    return key_times
