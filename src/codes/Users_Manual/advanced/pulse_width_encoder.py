~from pyautd3 import PulseWidthEncoder, PulseWidth
PulseWidthEncoder(lambda _dev: lambda i: PulseWidth.from_duty(i.value / 510.0))