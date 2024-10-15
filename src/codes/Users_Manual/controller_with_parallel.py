~# mypy: ignore-errors
~from pyautd3 import Controller, AUTD3, Static, Null
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
~m = Static()
~g = Null()
autd.send((m, g).with_parallel_threshold(0))