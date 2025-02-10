~from pyautd3 import AUTD3
from pyautd3_emulator import Emulator

with Emulator([AUTD3()]) as emulator:
    df = emulator.transducer_table()
    print(df)