~import numpy as np
from pyautd3 import AUTD3, Duration, Focus, FocusOption, Silencer, Static
from pyautd3_emulator import Emulator, RangeXYZ, Recorder, RmsRecordOption

with Emulator([AUTD3()]) as emulator:
    focus = emulator.center() + np.array([0.0, 0.0, 150.0])

    def f(autd: Recorder) -> None:
        autd.send(Silencer.disable())
        autd.send((Static(), Focus(pos=focus, option=FocusOption())))
        autd.tick(Duration.from_micros(25))

    record = emulator.record(f)

    sound_field = record.sound_field(
        RangeXYZ(
            x_start=focus[0] - 20.0,
            x_end=focus[0] + 20.0,
            y_start=focus[1] - 20.0,
            y_end=focus[1] + 20.0,
            z_start=focus[2],
            z_end=focus[2],
            resolution=1.0,
        ),
        RmsRecordOption(
            sound_speed=340e3,
            print_progress=True,
            gpu=False,
        ),
    )

    df = sound_field.observe_points()
    print(df)

    df = sound_field.next(Duration.from_micros(25))
    print(df)