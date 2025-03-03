~import numpy as np
~from pyautd3 import EmitIntensity
from pyautd3.gain.holo import Greedy, EmissionConstraint, GreedyOption, Pa

~x1 = 0.0
~y1 = 0.0
~z1 = 0.0
~x2 = 0.0
~y2 = 0.0
~z2 = 0.0
Greedy(
    foci=[(np.array([x1, y1, z1]), 5e3 * Pa), (np.array([x2, y2, z2]), 5e3 * Pa)],
    option=GreedyOption(
        phase_div=16,
        constraint=EmissionConstraint.Uniform(EmitIntensity.MAX),
    ),
)