~from pyautd3 import Intensity, Phase, Plane, PlaneOption
~nx = 1.0
~ny = 0.0
~nz = 0.0
Plane(
    direction=[nx, ny, nz],
    option=PlaneOption(
        intensity=Intensity.MAX,
        phase_offset=Phase.ZERO,
    ),
)