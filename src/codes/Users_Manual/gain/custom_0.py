~from pyautd3 import Drive, EmitIntensity, Phase
from pyautd3.gain import Custom

Custom(lambda _dev: lambda _tr: Drive(phase=Phase.ZERO, intensity=EmitIntensity.MIN))