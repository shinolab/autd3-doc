use autd3::core::derive::*;
# use autd3::prelude::*;

#[derive(Gain, Debug)]
pub struct FocalPoint {
    pos: Point3,
}

#[derive(Clone, Copy)]
pub struct Impl {
    pos: Point3,
    wavenumber: f32,
}

impl GainCalculator for Impl {
    fn calc(&self, tr: &Transducer) -> Drive {
        Drive {
            phase: Phase::from(-(self.pos - tr.position()).norm() * self.wavenumber * rad),
            intensity: Intensity::MAX,
        }
    }
}

impl GainCalculatorGenerator for Impl {
    type Calculator = Impl;

    fn generate(&mut self, _: &Device) -> Self::Calculator {
        *self
    }
}

impl Gain for FocalPoint {
    type G = Impl;

    fn init(
        self,
        _geometry: &Geometry,
        env: &Environment,
        _filter: &TransducerFilter,
    ) -> Result<Self::G, GainError> {
        Ok(Impl {
            pos: self.pos,
            wavenumber: env.wavenumber(),
        })
    }
}
# fn main() {}