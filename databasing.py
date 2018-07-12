
import pickle
from collections import Counter, namedtuple

class AudioDatabase:
	def __init__(self, filename):
		self.filename = filename;
		self.dictionary = {}
	def put(self, key, value):
		if key not in self.dictionary:
			self.dictionary[key] = []
		self.dictionary[key].append(value)
	def get(self, key):
		return self.dictionary.get(key, [])
	def save(self):	
		with open(self.filename, mode="wb") as file:
			pickle.dump(self.dictionary, file)
	def load(self):
		with open(self.filename, mode="rb") as file:
			self.dictionary = pickle.load(file)
	def store(self, fingerprints, song):
		for fingerprint in fingerprints:
			self.put((fingerprint.frequency1, fingerprint.frequency2, fingerprint.delta), (song, fingerprint.time))
	def predict(self, database, fingerprints):
		counter = Counter()
		for fingerprint in fingerprints:
			matches = self.get((fingerprint.frequency1, fingerprint.frequency2, fingerprint.delta))
			for match in matches:
				counter.update((match[0], match[1] - fingerprint.time))
		return counter.most_common()[0]

Fingerprint = namedtuple('Fingerprint', ['frequency1', 'frequency2', 'delta', 'time'])

