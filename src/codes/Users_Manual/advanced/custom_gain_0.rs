# use autd3::prelude::*;
use autd3::derive::*;

#[derive(Gain, Debug)]
pub struct FocalPoint {
    pos: Vector3,
}

pub struct Context {
    pos: Vector3,
    wavenumber: f32,
}

impl GainContext for Context {
    fn calc(&self, tr: &Transducer) -> Drive {
        (
            Phase::from(-(self.pos - tr.position()).norm() * self.wavenumber * rad),
            EmitIntensity::MAX,
        )
            .into()
    }
}

impl GainContextGenerator for FocalPoint {
    type Context = Context;

    fn generate(&mut self, device: &Device) -> Self::Context {
        Context {
            pos: self.pos,
            wavenumber: device.wavenumber(),
        }
    }
}

impl Gain for FocalPoint {
    type G = FocalPoint;

    fn init(
        self,
        _geometry: &Geometry,
        _filter: Option<&HashMap<usize, BitVec<u32>>>,
    ) -> Result<Self::G, AUTDInternalError> {
        Ok(self)
    }
}

# #[allow(unused_variables)]
# fn main() { 
# }