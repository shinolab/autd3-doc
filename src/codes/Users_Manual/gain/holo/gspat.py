~import numpy as np
~from pyautd3 import EmitIntensity
from pyautd3.gain.holo import GSPAT, EmissionConstraint, GSPATOption, NalgebraBackend, Pa

~x1 = 0.0
~y1 = 0.0
~z1 = 0.0
~x2 = 0.0
~y2 = 0.0
~z2 = 0.0
backend = NalgebraBackend()
GSPAT(
    foci=[(np.array([x1, y1, z1]), 5e3 * Pa), (np.array([x2, y2, z2]), 5e3 * Pa)],
    option=GSPATOption(
        repeat=100,
        constraint=EmissionConstraint.Clamp(EmitIntensity.MIN, EmitIntensity.MAX),
    ),
    backend=backend,
)