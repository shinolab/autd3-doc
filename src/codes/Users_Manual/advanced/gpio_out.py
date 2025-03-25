~from pyautd3 import GPIOOutputs, GPIOOutputType, GPIOOut
GPIOOutputs(
    lambda _dev, gpio: (
        GPIOOutputType.BaseSignal if gpio == GPIOOut.O0 else GPIOOutputType.NONE
    ),
)