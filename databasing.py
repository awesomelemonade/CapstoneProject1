
import pickle
from collections import Counter, namedtuple

class AudioDatabase:
	def __init__(self, filename):
		"""Initializes with a filename for the database to store to
		Parameters
		----------
			filename: String
				A String representing the file that it is supposed to store to
		"""
		self.filename = filename;
		self.dictionary = {}
	def put(self, key, value):
		"""Puts a pair of key and value into the dictionary"""
		if key not in self.dictionary:
			self.dictionary[key] = []
		self.dictionary[key].append(value)
	def get(self, key):
		"""Retrieves value based off key"""
		return self.dictionary.get(key, [])
	def save(self):
		"""Saves dictionary into file"""
		with open(self.filename, mode="wb") as file:
			pickle.dump(self.dictionary, file)
	def load(self):
		"""Loads dictionary from file"""
		with open(self.filename, mode="rb") as file:
			self.dictionary = pickle.load(file)
	def store(self, fingerprints, song):
		"""Stores fingerprints with a song id to dictionary
		Parameters
		----------
			fingerprints: List
				List of "Fingerprint" named tuples
			song: integer
				An integer representing the song id
		"""
		for fingerprint in fingerprints:
			self.put((fingerprint.frequency1, fingerprint.frequency2, fingerprint.delta), (song, fingerprint.time))
	def predict(self, fingerprints):
		"""Predicts a song id based off stored dictionary and fingerprints
		Parameters
		----------
			fingerprints: List
				List of "Fingerprint" named tuples
		Returns
		-------
			songId: integer
				An integer representing the song id
		"""
		counter = Counter()
		for fingerprint in fingerprints:
			matches = self.get((fingerprint.frequency1, fingerprint.frequency2, fingerprint.delta))
			for match in matches:
				counter.update((match[0], match[1] - fingerprint.time))
		return counter.most_common()[0]

Fingerprint = namedtuple('Fingerprint', ['frequency1', 'frequency2', 'delta', 'time'])

