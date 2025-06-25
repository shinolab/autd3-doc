~import numpy as np
~from pyautd3 import Intensity
from pyautd3.gain.holo import LM, EmissionConstraint, LMOption, NalgebraBackend, Pa

~x1 = 0.0
~y1 = 0.0
~z1 = 0.0
~x2 = 0.0
~y2 = 0.0
~z2 = 0.0
backend = NalgebraBackend()
LM(
    foci=[(np.array([x1, y1, z1]), 5e3 * Pa), (np.array([x2, y2, z2]), 5e3 * Pa)],
    option=LMOption(
        eps_1=1e-8,
        eps_2=1e-8,
        tau=1e-3,
        k_max=5,
        initial = None,
        constraint=EmissionConstraint.Clamp(Intensity.MIN, Intensity.MAX),
    ),
    backend=backend,
)