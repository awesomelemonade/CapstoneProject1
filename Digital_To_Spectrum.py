def dig_to_spec(data, fs):
    """Get the original data and returns the Spectrum, frequency and times associated with it

    Parameters
    ----------
        data: numpy.ndarray, shape = (M,)
            A 1-D array of the audio data
        fs: integer
            An integer representing the sampling_size

    Returns
    -------
        S: numpy.ndarray, shape = (N, W)
            A 2-D array that returns the magnitude of Fourier coefficients based on the data
        f: numpy.ndarray, shape = (N,)
            A 1-D array that returns the frequencies at index i for each row of S
        t: numpy.ndarray, shape = (W,)
            A 1-D array that returns the times at index i for each row of S
    """
    return mlab.specgram(data, NFFT=4096, Fs=fs,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)[0]


def spec_to_peaks(data, value, fp = generate_binary_structure(rank = 2, connectivity=2)):
    """Gets the data and the cutoff and return the true and false values of the max

    Parameters
    ----------
        data: numpy.ndarray, shape = (M, N)
            A 2-D array of the spectrum data
        value: integer
            Cutoff values
        fp: numpy.ndarray,  boolean [Optional]
            A 2-D array Fingerprint for the surrounding
    Returns
    -------
        isPeaks: numpy.ndarray, shape = (M, N)
            A 2-D array of true/false values of the data where peaks are located

    """

    max_arr = maximum_filter(data, footprint = fp)
    return (arr == max_arr) & (arr > value)
