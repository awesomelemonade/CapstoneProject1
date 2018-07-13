import databasing 
import peaks_to_fingerprints
import Digital_To_Spectrum
import digital_signal

def storeMP3toDatabase(directory, songId):
	data, sampling_rate = digital_signal.get_mp3_data(directory)
	spectrogram = Digital_To_Spectrum.dig_to_spec(data, sampling_rate)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, 0)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.store(fingerprints, songId)
	database.save()
def micMatch(duration):
	data, sampling_rate = digital_signal.get_microphone_dat(duration)
	spectrogram = Digital_To_Spectrm.dig_to_spec(data, sampling_rate)
	peaks = Digital_To_Spectrum.spec_to_peaks(spectrogram, 0)
	fingerprints = peaks_to_fingerprints.peaks_to_fingerprints(peaks, 15)
	database = databasing.AudioDatabase("database.whydoyoucareaboutthisextension")
	database.load()
	print(database.predict(fingerprints))

storeMP3toDatabase("./music/cake.mp3", 3)
storeMP3toDatabase("./music/taco.mp3", 2)

