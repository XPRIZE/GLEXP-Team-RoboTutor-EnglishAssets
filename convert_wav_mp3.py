from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
import sys

mypath = sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-4:] == ".wav"]

for f_wav in onlyfiles:
    f_root = f_wav[:-4]
    f_mp3 = f_root + ".mp3"
    f_in = join(mypath, f_wav)
    print f_in
    AudioSegment.from_wav(f_in).export(join(mypath, f_mp3), format="mp3")
