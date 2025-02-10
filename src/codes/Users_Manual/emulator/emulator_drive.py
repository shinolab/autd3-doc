from pyautd3 import (
    AUTD3,
    Duration,
    EmitIntensity,
    Hz,
    Phase,
    Silencer,
    Sine,
    SineOption,
    Uniform,
)
from pyautd3_emulator import Emulator, Recorder

with Emulator([AUTD3()]) as emulator:

    def f(autd: Recorder) -> None:
        autd.send(Silencer())
        autd.send(
            (
                Sine(freq=200.0 * Hz, option=SineOption()),
                Uniform(intensity=EmitIntensity.MAX, phase=Phase.ZERO),
            ),
        )
        autd.tick(Duration.from_millis(10))

    record = emulator.record(f)

    df = record.phase()
    print(df)

    df = record.pulse_width()
    print(df)