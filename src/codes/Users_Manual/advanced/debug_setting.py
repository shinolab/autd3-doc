~from pyautd3 import AUTD3, Controller, DebugSettings, DebugType, GPIOOut
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(
    DebugSettings(
        lambda _dev, gpio: (
            DebugType.BaseSignal if gpio == GPIOOut.O0 else DebugType.NONE
        ),
    ),
)