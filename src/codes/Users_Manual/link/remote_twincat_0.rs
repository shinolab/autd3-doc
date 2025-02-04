use autd3_link_twincat::remote::{RemoteTwinCAT, RemoteTwinCATOption};

# fn main() {
# let _ = 
RemoteTwinCAT::new("0.0.0.0.0.0", RemoteTwinCATOption {
    server_ip: "".to_string(),
    client_ams_net_id: "".to_string(),
});
# }