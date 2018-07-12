def dig_to_spec(data, fs):
    fig, ax = plt.subplots()
    S, freqs, times = m.specgram(data, NFFT=4096, Fs=fs,
                                  window=mlab.window_hanning,
                                  noverlap=4096 // 2)
    fig.colorbar(im)
    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Frequency (Hz)")
    ax.set_title("Spectrogram of Trumpet")
    ax.set_ylim(0, 6000);
    return S

def spec_to_peaks(data, value, fp = generate_binary_structure(rank = 2, connectivity=2)):
    max_arr = maximum_filter(data, footprint = fp)
    return (arr == max_arr) & (arr > value)
