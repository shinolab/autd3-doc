~import pathlib
~
~from pyautd3 import kHz
~from pyautd3.modulation import BlackMan, SincInterpolation
~from pyautd3.modulation.audio_file import Csv
~
~path = pathlib.Path("path/to/foo.wav")
m = Csv.new_with_resample(
    path, 2.0 * kHz, 4 * kHz, SincInterpolation(BlackMan(32)),
)