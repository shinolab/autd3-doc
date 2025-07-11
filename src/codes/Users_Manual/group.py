~from pyautd3 import Device, Group
~from pyautd3.gain import Focus, FocusOption, Null
~x = 0.0
~y = 0.0
~z = 0.0
def key_map(dev: Device) -> str | None:
    if dev.idx == 0:
        return "null"
    if dev.idx == 1:
        return "focus"
    return None


Group(
    key_map=key_map,
    data_map={"null": Null(), "focus": Focus(pos=[x, y, z], option=FocusOption())},
)