~from pyautd3 import AUTD3, Controller, Segment, SwapSegment, TransitionMode
~from pyautd3.link.nop import Nop
~autd = Controller.open([AUTD3()], Nop())
autd.send(SwapSegment.Modulation(Segment.S1, TransitionMode.Immediate))