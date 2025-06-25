~from pyautd3 import Drive, Intensity, Phase
from pyautd3.gain import Custom

Custom(lambda _dev: lambda _tr: Drive(phase=Phase.ZERO, intensity=Intensity.MIN))