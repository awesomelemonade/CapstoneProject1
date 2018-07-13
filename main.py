import databasing 
import peaks_to_fingerprints
import Digital_To_Spectrum
import digital_signal


import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def storeMP3toDatabase(directory, songId):
	data, sampling_rate = digital_signal.get_mp3_data(directory)
	spectrogram = Digital_To_Spectrum.dig_to_spec(data, sampling_rate)
	threshold = np.percentile(spectrogram, 90)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, threshold)
	print(threshold)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	print(fingerprints.shape)
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.store(fingerprints, songId)
	database.save()
def micMatch(duration):
	data, sampling_rate = digital_signal.get_microphone_data(duration)
	spectrogram = Digital_To_Spectrum.dig_to_spec(data, sampling_rate)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, 0)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	print(fingerprints.shape)
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.load()
	print(database.predict(fingerprints))
def load():
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.load()

import os

directory = "./music/"
#for index, filename in enumerate(os.listdir(directory)):
#	print("Storing MP3: "+filename+" - "+str(index))
#	storeMP3toDatabase(directory + filename, index)

storeMP3toDatabase("./music/taco.mp3", 0)

#load()

#micMatch(10)

