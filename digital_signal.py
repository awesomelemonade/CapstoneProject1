
# coding: utf-8

# In[5]:


import numpy as np
import microphone
import librosa


# In[2]:


def get_microphone_data(listen_time):
    '''
    Parameters:
        listen_time - in seconds
    Returns:
        audio_data - digital audio signal as numpy array
        sampling_rate - in Hertz
    '''
    frames, sampling_rate = microphone.record_audio(listen_time)
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    return audio_data, sampling_rate


# In[62]:


def get_mp3_data(file_path):
    '''
    Parameters:
        file_path - string
    Returns:
        audio_data - digital audio signal as numpy array
        sampling_rate - in Hertz
    '''
    from pathlib import Path
    audio_data, sampling_rate = librosa.load(Path(file_path), sr=44100, mono=True)
    audio_data = (audio_data*(2**15)).astype('int16')
    return audio_data, sampling_rate

