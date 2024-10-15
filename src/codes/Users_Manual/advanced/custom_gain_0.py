import numpy as np
from pyautd3 import Drive, EmitIntensity, Geometry, Phase, rad
from pyautd3.gain import Gain


class Focus(Gain):
    def __init__(self, point):
        self.point = np.array(point)

    def calc(self, _: Geometry):
        return Gain._transform(
            lambda dev: lambda tr: Drive(
                (
                    Phase(
                        float(-np.linalg.norm(tr.position - self.point))
                        * dev.wavenumber
                        * rad
                    ),
                    EmitIntensity.maximum(),
                ),
            ),
        )
