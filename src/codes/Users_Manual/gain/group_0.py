~from pyautd3 import Focus, FocusOption, Group, Null
~x = 1.0
~y = 0.0
~z = 0.0
Group(
    key_map=lambda _: lambda tr: "null" if tr.idx() <= 100 else "focus",
    gain_map={"null": Null(), "focus": Focus(pos=[x, y, z], option=FocusOption())},
)