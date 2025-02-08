~import pathlib
~from pyautd3 import Hz
from pyautd3.modulation.audio_file import Csv, CsvOption

path = pathlib.Path("path/to/foo.csv")
m = Csv(path=path, sampling_config=4000 * Hz, option=CsvOption(deliminator=","))