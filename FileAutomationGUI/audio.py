from pydub import AudioSegment
import glob
import sys
import os

# Glob module is used to find files in a directory.
# Sys module is used to access system parameters and methods.
# Os module is used to access operating system specific functions.

class Audio:
    def __init__(self, infiles, dst):
        self.combined = AudioSegment.empty()
        self.infiles = infiles
        self.outfile = dst

    def process(self):
        for file in self.infiles:
            print(file)
            aud = AudioSegment.from_mp3(file)
            self.combined += aud

        self.combined.export(out_f=self.outfile, format="mp3")

# AudioSegment.from_mp3('D:\\backup\\Tora-Mann-Darpan-Kehlaye-beautiful-krishna-Bhajan-By-Asha-Bhonsle.mp3')

# AudioSegment.ffmpeg = os.getcwd()+"\\ffmpeg\\bin\\ffmpeg.exe"
# print (AudioSegment.ffmpeg)

# from pyffmpeg import FFmpeg
#
# inp = 'path/to/music_folder/f.mp4'
# out = 'path/to/music_folder/f.mp3'
#
# ff = FFmpeg().
# print(ff)
# output_file = "\\ffmpeg\\bin\\ffmpeg.exe"+ff.convert(inp, out)
#
# print(output_file)