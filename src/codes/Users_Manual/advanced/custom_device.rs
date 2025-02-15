use autd3::driver::geometry::{Device, IntoDevice, Transducer};
# use autd3::prelude::*;
# use autd3_emulator::Emulator;

struct CustomDevice {
    pitch: f32,
    num_x: usize,
    num_y: usize,
}

impl IntoDevice for CustomDevice {
    fn into_device(self, dev_idx: u16) -> Device {
        assert!(0 < self.num_x * self.num_y && self.num_x * self.num_y <= 256);
        Device::new(
            dev_idx,
            UnitQuaternion::identity(),
            itertools::iproduct!(0..self.num_x, 0..self.num_y)
                .enumerate()
                .map(|(i, (x, y))| {
                    let x = x as f32 * self.pitch;
                    let y = y as f32 * self.pitch;
                    Transducer::new(i as u8, dev_idx, Point3::new(x, y, 0.))
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