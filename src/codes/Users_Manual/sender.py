~from pyautd3 import AUTD3, Controller, Duration, Null, SenderOption
~from pyautd3.controller import SpinSleeper
~from pyautd3.link.nop import Nop
~from pyautd3.native_methods.autd3 import ParallelMode
autd = Controller.open([AUTD3()], Nop())
sender = autd.sender(
    SenderOption(
        send_interval=Duration.from_millis(1),
        receive_interval=Duration.from_millis(1),
        timeout=None,
        parallel=ParallelMode.Auto,
        sleeper=SpinSleeper(),
    )
)
~d = Null()
sender.send(d)