~from pyautd3 import EmitIntensity, Bessel
~x = 0.0
~y = 0.0
~z = 0.0
~nx = 1.0
~ny = 0.0
~nz = 0.0
~theta = 0.0
g = Bessel([x, y, z], [nx, ny, nz], theta).with_intensity(EmitIntensity.maximum())