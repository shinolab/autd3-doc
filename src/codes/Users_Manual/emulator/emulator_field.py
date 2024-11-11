~import numpy as np
from pyautd3 import AUTD3, Controller, Focus, Silencer, Static, Duration
from pyautd3.emulator import Range, Recorder, InstantRecordOption

with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).into_emulator() as emulator:
    focus = emulator.center + np.array([0.0, 0.0, 150.0])

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer.disable())
        autd.send((Static.with_intensity(0xFF), Focus(focus)))
        autd.tick(Duration.from_millis(1))
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
        InstantRecordOption(
            sound_speed=340e3,
            time_step=Duration.from_micros(1),
            print_progress=True,
            memory_limits_hint_mb=128,
            gpu=True,
        ),
    )
    df = sound_field.skip(Duration.from_micros(500)).next(
        Duration.from_micros(500),
    )
    print(df)