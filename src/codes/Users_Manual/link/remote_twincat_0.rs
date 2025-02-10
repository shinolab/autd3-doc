use autd3_link_twincat::remote::{RemoteTwinCAT, RemoteTwinCATOption};

# fn main() {
# let _ = 
RemoteTwinCAT::new("172.16.99.111.1.1", RemoteTwinCATOption {
    server_ip: "172.16.99.104".to_string(),
    client_ams_net_id: "172.16.99.62.1.1".to_string(),
});
# }