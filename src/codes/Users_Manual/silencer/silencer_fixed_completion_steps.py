~from pyautd3 import Duration, FixedCompletionTime, Silencer
config = Silencer(
    FixedCompletionTime(
        intensity=Duration.from_micros(250),
        phase=Duration.from_micros(250),
    ),
)