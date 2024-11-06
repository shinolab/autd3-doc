~from pyautd3.gain import Focus, Null
~from pyautd3 import Controller, AUTD3, Device
~from pyautd3.link.audit import Audit
~autd = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
~x = 0.0
~y = 0.0
~z = 0.0
def grouping(dev: Device) -> str | None:
    if dev.idx == 0:
        return "null"
    if dev.idx == 1:
        return "focus"
    return None

autd.group(grouping).set("null", Null()).set("focus", Focus([x, y, z])).send()