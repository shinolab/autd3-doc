~from datetime import timedelta
from pyautd3 import AUTD3, Controller, EmitIntensity,  Silencer,  Uniform, Static, Phase
from pyautd3.emulator import Emulator, Recorder

with Emulator([AUTD3([0.0, 0.0, 0.0])]) as emulator:

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer.disable())
        autd.send((Static.with_intensity(0xFF), Uniform((Phase(0x40), EmitIntensity(0xFF)))))
        autd.tick(timedelta(milliseconds=1))
        return autd

    record = emulator.record(f)

    df = record.output_ultrasound()
    print(df)