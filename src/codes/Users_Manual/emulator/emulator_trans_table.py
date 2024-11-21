~from pyautd3 import AUTD3, Controller
~import pyautd3.emulator # noqa: F401
with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).into_emulator() as emulator:
    df = emulator.transducer_table()
    print(df)