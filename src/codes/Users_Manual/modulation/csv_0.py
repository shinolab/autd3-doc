~import pathlib
~from pyautd3 import Hz
from pyautd3.modulation.audio_file import Csv, CsvOption

Csv(
    path=pathlib.Path("path/to/foo.csv"),
    sampling_config=4000 * Hz,
    option=CsvOption(
        delimiter=",",
    ),
)