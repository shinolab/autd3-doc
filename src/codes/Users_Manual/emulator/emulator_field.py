~from datetime import timedelta
~
~import numpy as np
from pyautd3 import AUTD3, Controller, Focus, Silencer, Static
from pyautd3.emulator import Range, Recorder, RecordOption

with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).into_emulator() as emulator:
    focus = emulator.center + np.array([0.0, 0.0, 150.0])

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer.disable())
        autd.send((Static.with_intensity(0xFF), Focus(focus)))
        autd.tick(timedelta(milliseconds=1))
        return autd

    record = emulator.record(f)

    sound_field = record.sound_field(
        Range(
            x_start=focus[0] - 20.0,
            x_end=focus[0] + 20.0,
            y_start=focus[1] - 20.0,
            y_end=focus[1] + 20.0,
            z_start=focus[2],
            z_end=focus[2],
            resolution=1.0,
        ),
        RecordOption(
            time_step_ns=1000,
            print_progress=True,
            gpu=True,
        ),
    )
    df = sound_field.skip(timedelta(microseconds=500)).next(
        timedelta(microseconds=500),
    )
    print(df)