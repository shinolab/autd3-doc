~from pyautd3 import Bessel, BesselOption, Intensity, Phase, rad
~
~x = 0.0
~y = 0.0
~z = 0.0
~nx = 1.0
~ny = 0.0
~nz = 0.0
~theta = 0.0
Bessel(
    apex=[x, y, z],
    direction=[nx, ny, nz],
    theta=theta * rad,
    option=BesselOption(
        intensity=Intensity.MAX,
        phase_offset=Phase.ZERO,
    ),
)