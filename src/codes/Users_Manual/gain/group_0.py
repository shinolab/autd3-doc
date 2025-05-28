~from pyautd3 import Focus, FocusOption, Null
from pyautd3.gain import Group
~x = 1.0
~y = 0.0
~z = 0.0
Group(
    key_map=lambda _: lambda tr: "null" if tr.idx() <= 100 else "focus",
    gain_map={"null": Null(), "focus": Focus(pos=[x, y, z], option=FocusOption())},
)