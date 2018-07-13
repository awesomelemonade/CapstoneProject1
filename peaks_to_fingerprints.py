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
    freqs, times = np.where(peaks)

    # creates list to return
    key_times = list()

    # for loop for fanout -- OPTIMIZED NOW, BLESS YOU ANNA
    for j in range(1, fanout):
        f1 = freqs[:len(freqs) - j] # frequency 1
        f2 = freqs[j:] # frequency 2
        delta_t = times[j:] - times[:len(times) - j] # change between time 2 and time 1
        t1 = times[:len(times) - j] # time 1
        # OMG BLESS YOU ANNA YOU MANAGED TO MAKE THIS OPTIMIZED
        key_times = np.vstack((f1, f2, delta_t, t1)).T
        key_times = list(tuple(zip(map(tuple, key_times[:,:3]), key_times[:, 3]))) # had to get rid of the named tuple for formatting, to be fixed
    return key_times
