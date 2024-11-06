~from datetime import timedelta
~
~from pyautd3 import FixedCompletionTime, Silencer
~
config = Silencer(
    FixedCompletionTime(
        intensity=timedelta(microseconds=250),
        phase=timedelta(microseconds=250),
    ),
)