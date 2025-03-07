use autd3::driver::geometry::{Device, Transducer};
# use autd3::prelude::*;
# use autd3_emulator::Emulator;

struct CustomDevice {
    pitch: f32,
    num_x: usize,
    num_y: usize,
}

impl From<CustomDevice> for Device {
    fn from(dev: CustomDevice) -> Self {
        assert!(0 < dev.num_x * dev.num_y && dev.num_x * dev.num_y <= 256);
        Device::new(
            UnitQuaternion::identity(),
            itertools::iproduct!(0..dev.num_x, 0..dev.num_y)
                .map(|(x, y)| {
                    let x = x as f32 * dev.pitch;
                    let y = y as f32 * dev.pitch;
                    Transducer::new(Point3::new(x, y, 0.))
                })
                .collect(),
        )
    }
}

# fn main() {
Emulator::new(
    [CustomDevice {
        pitch: 2.,
        num_x: 16,
        num_y: 16,
    }],
);
# }