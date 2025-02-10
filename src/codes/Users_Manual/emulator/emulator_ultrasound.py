from pyautd3 import AUTD3, Duration, EmitIntensity, Phase, Silencer, Static, Uniform
from pyautd3_emulator import Emulator, Recorder

with Emulator([AUTD3()]) as emulator:

    def f(autd: Recorder) -> None:
        autd.send(Silencer.disable())
        autd.send((Static(), Uniform(phase=Phase(0x40), intensity=EmitIntensity.MAX)))
        autd.tick(Duration.from_millis(1))

    record = emulator.record(f)

    df = record.output_ultrasound()
    print(df)