use autd3_link_remote::{Remote, RemoteOption};

# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _ = 
Remote::new("127.0.0.1:8080".parse()?, RemoteOption { timeout: None });
# Ok(())
# }