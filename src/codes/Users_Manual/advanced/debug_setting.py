~from pyautd3 import DebugSettings, DebugType, GPIOOut
DebugSettings(
    lambda _dev, gpio: (
        DebugType.BaseSignal if gpio == GPIOOut.O0 else DebugType.NONE
    ),
)