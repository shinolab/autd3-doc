use autd3::core::derive::*;
# use autd3::prelude::*;

#[derive(Gain, Debug)]
pub struct FocalPoint {
    pos: Point3,
}

pub struct Impl {
    pos: Point3,
    wavenumber: f32,
}

impl GainCalculator for Impl {
    fn calc(&self, tr: &Transducer) -> Drive {
        Drive {
            phase: Phase::from(-(self.pos - tr.position()).norm() * self.wavenumber * rad),
            intensity: EmitIntensity::MAX,
        }
    }
}

impl GainCalculatorGenerator for FocalPoint {
    type Calculator = Impl;

    fn generate(&mut self, device: &Device) -> Self::Calculator {
        Impl {
            pos: self.pos,
            wavenumber: device.wavenumber(),
        }
    }
}

impl Gain for FocalPoint {
    type G = FocalPoint;

    fn init(self) -> Result<Self::G, GainError> {
        Ok(self)
    }
}

# fn main() {}