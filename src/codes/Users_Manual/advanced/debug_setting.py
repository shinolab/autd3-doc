~from pyautd3 import AUTD3, Controller, DebugSettings, DebugType, GPIOOut
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(
    DebugSettings(
        lambda _dev, gpio: (
            DebugType.BaseSignal if gpio == GPIOOut.O0 else DebugType.NONE
        ),
    ),
)