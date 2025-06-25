~from pyautd3 import AUTD3, Controller, Duration, Null, SenderOption, FixedSchedule, ParallelMode
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
sender = autd.sender(
    SenderOption(
        send_interval=Duration.from_millis(1),
        receive_interval=Duration.from_millis(1),
        timeout=None,
        parallel=ParallelMode.Auto,
        strict=True
    ),
    FixedSchedule(),
)
~d = Null()
sender.send(d)