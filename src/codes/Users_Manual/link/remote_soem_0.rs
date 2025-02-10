use autd3_link_soem::RemoteSOEM;

# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let _ = 
RemoteSOEM::new("172.16.99.104:8080".parse()?);
# Ok(())
# }