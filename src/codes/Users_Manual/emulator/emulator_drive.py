from pyautd3 import (
    AUTD3,
    Controller,
    Duration,
    EmitIntensity,
    Hz,
    Silencer,
    Sine,
    Uniform,
)
from pyautd3.emulator import Recorder

with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).into_emulator() as emulator:

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer())
        autd.send((Sine(200.0 * Hz), Uniform(EmitIntensity(0xFF))))
        autd.tick(Duration.from_millis(10))
        return autd

    record = emulator.record(f)

    df = record.phase()
    print(df)

    df = record.pulse_width()
    print(df)