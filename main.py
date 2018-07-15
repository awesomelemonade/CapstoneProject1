import databasing 
import peaks_to_fingerprints
import Digital_To_Spectrum
import digital_signal
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def storeMP3toDatabase(directory, songId):
	data, sampling_rate = digital_signal.get_mp3_data(directory)
	spectrogram = Digital_To_Spectrum.dig_to_spec(data, sampling_rate)
	threshold = np.percentile(spectrogram, 30)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, threshold)
	print(threshold)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	print(fingerprints.shape)
	return fingerprints
def micMatch(duration, database):
	data, sampling_rate = digital_signal.get_microphone_data(duration)
	spectrogram = Digital_To_Spectrum.dig_to_spec(data, sampling_rate)
	threshold = np.percentile(spectrogram, 30)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, threshold)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	print(fingerprints.shape)
	print(database.predict(fingerprints))
def load():
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.load()

import os


database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
"""
directory = "./music/"
for index, filename in enumerate(os.listdir(directory)):
	print("Storing MP3: "+filename+" - "+str(index))
	fingerprints = storeMP3toDatabase(directory + filename, index)
	database.store(fingerprints, index)

database.save()
"""
database.load()

while(True):
	input("Waiting...")
	micMatch(10, database)

#storeMP3toDatabase("./music/taco.mp3", 0)

#load()

