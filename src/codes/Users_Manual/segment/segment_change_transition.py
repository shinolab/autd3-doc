~from pyautd3 import Segment, SwapSegment
~from pyautd3 import Controller, AUTD3, TransitionMode
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
autd.send(SwapSegment.modulation(Segment.S1, TransitionMode.Immediate))