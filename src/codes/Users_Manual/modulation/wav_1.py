~import pathlib
~from pyautd3 import kHz
~from pyautd3.modulation import SincInterpolation, BlackMan
~from pyautd3.modulation.audio_file import Wav
~path = pathlib.Path("path/to/foo.wav")
m = Wav.new_with_resample(path, 4 * kHz, SincInterpolation(BlackMan(32)))