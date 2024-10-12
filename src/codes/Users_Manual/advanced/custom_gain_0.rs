use autd3::prelude::*;
use autd3::derive::*;

#[derive(Gain, Debug)]
pub struct FocalPoint {
    position: Vector3,
}

impl FocalPoint {
    pub fn new(position: Vector3) -> Self {
        Self { position }
    }
}

impl Gain for FocalPoint {
    fn calc(&self, _geometry: &Geometry) -> Result<GainCalcFn, AUTDInternalError> {
        let position = self.position;
        Ok(Self::transform(move |dev| {
            let wavenumber = dev.wavenumber();
            move |tr| {
                Drive::new(
                    Phase::from(-(position - tr.position()).norm() * wavenumber * rad),
                    EmitIntensity::MAX,
                )
            }
        }))
    }
}
# #[allow(unused_variables)]
# fn main() { 
# }