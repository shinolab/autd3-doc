from pyautd3 import (
    AUTD3,
    Controller,
    Duration,
    EmitIntensity,
    Phase,
    Silencer,
    Static,
    Uniform,
)
from pyautd3.emulator import Recorder

with Controller.builder([AUTD3([0.0, 0.0, 0.0])]).into_emulator() as emulator:

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer.disable())
        autd.send(
            (
                Static.with_intensity(0xFF),
                Uniform((Phase(0x40), EmitIntensity(0xFF))),
            ),
        )
        autd.tick(Duration.from_millis(1))
        return autd

    record = emulator.record(f)

    df = record.output_voltage()
    print(df)