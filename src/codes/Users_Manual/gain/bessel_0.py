~from pyautd3 import Bessel, BesselOption, EmitIntensity, Phase, rad
~
~x = 0.0
~y = 0.0
~z = 0.0
~nx = 1.0
~ny = 0.0
~nz = 0.0
~theta = 0.0
Bessel(
    pos=[x, y, z],
    direction=[nx, ny, nz],
    theta=theta * rad,
    option=BesselOption(
        intensity=EmitIntensity.MAX,
        phase_offset=Phase.ZERO,
    ),
)