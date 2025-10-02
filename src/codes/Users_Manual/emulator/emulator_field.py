~import numpy as np
from pyautd3 import AUTD3, Focus, FocusOption, Silencer, Static, Duration
from pyautd3_emulator import Emulator, RangeXYZ, Recorder, InstantRecordOption

with Emulator([AUTD3()]) as emulator:
    focus = emulator.center() + np.array([0.0, 0.0, 150.0])

    def f(autd: Recorder) -> None:
        autd.send(Silencer.disable())
        autd.send((Static(), Focus(pos=focus, option=FocusOption())))
        autd.tick(Duration.from_millis(1))

    record = emulator.record(f)

    sound_field = record.sound_field(
        RangeXYZ(
            x=(focus[0] - 20.0, focus[0] + 20.0),
            y=(focus[1] - 20.0, focus[1] + 20.0),
            z=(focus[2], focus[2]),
            resolution=1.0,
        ),
        InstantRecordOption(
            sound_speed=340e3,
            time_step=Duration.from_micros(1),
            memory_limits_hint_mb=128,
            gpu=True,
        ),
    )

    df = sound_field.observe_points()
    print(df)

    df = sound_field.skip(Duration.from_micros(500)).next(
        Duration.from_micros(500),
    )
    print(df)