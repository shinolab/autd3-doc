~from datetime import timedelta
from pyautd3 import AUTD3, Controller, EmitIntensity, Hz, Silencer, Sine, Uniform
from pyautd3.emulator import Emulator, Recorder

with Emulator([AUTD3([0.0, 0.0, 0.0])]) as emulator:

    def f(autd: Controller[Recorder]) -> Controller[Recorder]:
        autd.send(Silencer())
        autd.send((Sine(200.0 * Hz), Uniform(EmitIntensity(0xFF))))
        autd.tick(timedelta(milliseconds=10))
        return autd

    record = emulator.record(f)

    df = record.drive()
    print(df)