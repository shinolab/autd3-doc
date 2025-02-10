~from pyautd3 import Duration, FixedCompletionTime, Silencer, SilencerTarget
Silencer(
    config=FixedCompletionTime(
        intensity=Duration.from_micros(250),
        phase=Duration.from_micros(250),
        strict_mode=True,
    ),
    target=SilencerTarget.Intensity,
)