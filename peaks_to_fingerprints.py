# imports
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
            int."""
def peaks_to_fingerprints(peaks, fanout):
    # gets two arrays, frequency and time. Use np.where on peaks
    freqs, times = np.where(peaks)

    # creates list to return
    key_times = list()

    # for loop for fanout
    for j in range(fanout - 1):
        f1 = freqs[j:len(times) - j - 1] # frequency 1
        f2 = freqs[j + 1:len(times) - j] # frequency 2
        delta_t = times[j + 1:len(times) - j] - times[j:len(times) - j - 1] # change between time 2 and time 1
        t1 = times[j:len(times) - j - 1] # time 1
        # loops through each element, MAY NEED TO BE OPTIMIZED
        for i in range(len(f1)):
            key_times.append(((f1[i], f2[i], delta_t[i]), t1[i])) # adds the tuple to the list
    return keys_times
