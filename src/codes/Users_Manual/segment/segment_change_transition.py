~from pyautd3 import AUTD3, Controller, Segment, SwapSegment, TransitionMode
~from pyautd3.link.audit import Audit
~
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(SwapSegment.Modulation(Segment.S1, TransitionMode.Immediate))