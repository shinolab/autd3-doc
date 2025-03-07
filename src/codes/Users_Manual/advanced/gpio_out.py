~from pyautd3 import GPIOOutputs, DebugType, GPIOOut
GPIOOutputs(
    lambda _dev, gpio: (
        DebugType.BaseSignal if gpio == GPIOOut.O0 else DebugType.NONE
    ),
)