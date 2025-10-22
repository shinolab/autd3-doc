use autd3_link_twincat::{RemoteTwinCAT, RemoteTwinCATOption, Source, Timeouts};

# fn main() -> Result<(), Box<dyn std::error::Error>> {
#     let _ = 
RemoteTwinCAT::new(
    "0.0.0.0".parse()?,
    "1.1.1.1.1.1".parse()?,
    RemoteTwinCATOption {
        timeouts: Timeouts::none(),
        source: Source::Auto,
    },
);
# Ok(())
# }