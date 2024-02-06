'''
output:

{
  "jsonrpc": "2.0",
  "result": {
    "body": {
      "TABLE_nve_peers": {
        "ROW_nve_peers": [
          {
            "detail": 1,
            "if-name": "nve1",
            "peer-ip": "10.3.0.1",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:26:13",
            "router-mac": "3c13.cc2e.e087",
            "first-vni": 2097152,
            "create-ts": "22:26:13",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "2097152",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "FABRIC"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.3.0.2",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:29:08",
            "router-mac": "0200.0a03.0002",
            "first-vni": 2097152,
            "create-ts": "22:29:08",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "2097152,14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "FABRIC"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.3.0.3",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:26:15",
            "router-mac": "3c13.cc2e.de47",
            "first-vni": 2097152,
            "create-ts": "22:26:15",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "2097152",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "FABRIC"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.3.0.5",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:25:57",
            "router-mac": "n/a",
            "first-vni": 14680064,
            "create-ts": "22:25:57",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "FABRIC"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.13.0.3",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:25:57",
            "router-mac": "n/a",
            "first-vni": 14680064,
            "create-ts": "22:25:57",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "DCI"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.13.0.4",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:25:57",
            "router-mac": "n/a",
            "first-vni": 14680064,
            "create-ts": "22:25:57",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "DCI"
          },
          {
            "if-name": "nve1",
            "peer-ip": "10.23.0.1",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:25:57",
            "router-mac": "n/a",
            "first-vni": 14680064,
            "create-ts": "22:25:57",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "DCI"
          },
          {
            "if-name": "nve1",
            "peer-ip": "100.10.0.2",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:29:08",
            "router-mac": "0200.640a.0002",
            "first-vni": 2097152,
            "create-ts": "22:29:08",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "2097152,14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "DCI"
          },
          {
            "if-name": "nve1",
            "peer-ip": "100.10.0.3",
            "peer-state": "Up",
            "learn-type": "CP",
            "uptime": "22:25:59",
            "router-mac": "0200.640a.0003",
            "first-vni": 14680064,
            "create-ts": "22:25:59",
            "config-vnis": "2097152,14680064",
            "provision-state": "peer-add-complete",
            "cp-vni": "2097152,14680064",
            "vni-assignment-mode": "SYMMETRIC",
            "dci-fabric-location": "DCI"
          }
        ]
      }
    }
  },
  "id": 1
}

'''

def createMo(output):
    from nxapi.model.nve.Peer import nvePeer
    mos = []
    def parsePeer(peer):
        peerMo = nvePeer()
        peerMo.peer_ip = peer['peer-ip']
        peerMo.peer_state = peer['peer-state']
        peerMo.learn_type = peer['learn-type']
        peerMo.uptime = peer['uptime']
        peerMo.router_mac = peer['router-mac']
        peerMo.first_vni = peer['first-vni']
        peerMo.create_ts = peer['create-ts']
        peerMo.config_vnis = peer['config-vnis']
        peerMo.provision_state = peer['provision-state']
        peerMo.cp_vni = peer['cp-vni']
        peerMo.vni_assignment_mode = peer['vni-assignment-mode']
        peerMo.dci_fabric_location = peer['dci-fabric-location']
        return peerMo
    if 'TABLE_nve_peers' in output:
        if 'ROW_nve_peers' in output['TABLE_nve_peers']:
            for peer in output['TABLE_nve_peers']['ROW_nve_peers']:
                mos.append(parsePeer(peer))
    return mos