~from pyautd3 import Silencer, SilencerTarget, FixedUpdateRate
Silencer(
    config=FixedUpdateRate(
        intensity=1,
        phase=1,
    ),
    target=SilencerTarget.Intensity,
)