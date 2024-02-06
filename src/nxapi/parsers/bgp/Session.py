'''
show bgp sessions vrf default

output:
 {
      "totalpeers": 6,
      "totalestablishedpeers": 6,
      "localas": 100,
      "TABLE_vrf": {
        "ROW_vrf": {
          "vrf-name-out": "default",
          "local-as": 100,
          "vrfpeers": 6,
          "vrfestablishedpeers": 6,
          "router-id": "10.2.0.3",
          "TABLE_neighbor": {
            "ROW_neighbor": [
              {
                "neighbor-id": "10.2.0.4",
                "connectionsdropped": 0,
                "remoteas": 100,
                "lastflap": "P10DT21H46M15S",
                "lastread": "PT2S",
                "lastwrite": "PT57S",
                "state": "Established",
                "localport": 179,
                "remoteport": 57590,
                "notificationssent": 0,
                "notificationsreceived": 0
              },
              {
                "neighbor-id": "10.12.0.4",
                "connectionsdropped": 0,
                "remoteas": 101,
                "lastflap": "P8DT20H40M53S",
                "lastread": "PT45S",
                "lastwrite": "PT47S",
                "state": "Established",
                "localport": 55970,
                "remoteport": 179,
                "notificationssent": 0,
                "notificationsreceived": 0
              },
              {
                "neighbor-id": "10.12.0.5",
                "connectionsdropped": 0,
                "remoteas": 101,
                "lastflap": "P8DT20H40M43S",
                "lastread": "PT45S",
                "lastwrite": "PT47S",
                "state": "Established",
                "localport": 179,
                "remoteport": 28626,
                "notificationssent": 0,
                "notificationsreceived": 0
              },
              {
                "neighbor-id": "10.22.0.1",
                "connectionsdropped": 0,
                "remoteas": 102,
                "lastflap": "PT22H56M33S",
                "lastread": "PT58S",
                "lastwrite": "PT47S",
                "state": "Established",
                "localport": 18962,
                "remoteport": 179,
                "notificationssent": 0,
                "notificationsreceived": 0
              },
              {
                "neighbor-id": "102.10.0.1",
                "connectionsdropped": 0,
                "remoteas": 500,
                "lastflap": "P8DT20H40M54S",
                "lastread": "PT56S",
                "lastwrite": "PT10S",
                "state": "Established",
                "localport": 16152,
                "remoteport": 179,
                "notificationssent": 0,
                "notificationsreceived": 0
              },
              {
                "neighbor-id": "102.10.0.5",
                "connectionsdropped": 0,
                "remoteas": 500,
                "lastflap": "P8DT20H40M55S",
                "lastread": "PT56S",
                "lastwrite": "PT10S",
                "state": "Established",
                "localport": 43248,
                "remoteport": 179,
                "notificationssent": 0,
                "notificationsreceived": 0
              }
            ]
          }
        }
      }
    }
'''

def createMo(output):
    from nxapi.model.bgp.Session import bgpSession
    mos = []
    def parseVrf(vrf):
        MoList = []
        
        for neighbor in vrf['TABLE_neighbor']['ROW_neighbor']:
            vrfKwargs = {}
            vrfKwargs['vrf_name'] = vrf['vrf-name-out']
            vrfKwargs['local_as'] = vrf['local-as']
            vrfKwargs['vrf_peers'] = vrf['vrfpeers']
            vrfKwargs['vrf_established_peers'] = vrf['vrfestablishedpeers']
            vrfKwargs['router_id'] = vrf['router-id']
            MoList.append(parseNeighbor(neighbor,vrfKwargs))
            
        return MoList
    
    def parseNeighbor(neighbor,vrfKwargs):
        neighborMo = bgpSession()
        for key,value in vrfKwargs.items():
            setattr(neighborMo,key,value)
        neighborMo.neighbor_id = neighbor['neighbor-id']
        neighborMo.connections_dropped = neighbor['connectionsdropped']
        neighborMo.remote_as = neighbor['remoteas']
        neighborMo.last_flap = neighbor['lastflap']
        neighborMo.last_read = neighbor['lastread']
        neighborMo.last_write = neighbor['lastwrite']
        neighborMo.state = neighbor['state']
        neighborMo.local_port = neighbor['localport']
        neighborMo.remote_port = neighbor['remoteport']
        neighborMo.notifications_sent = neighbor['notificationssent']
        neighborMo.notifications_received = neighbor['notificationsreceived']
        return neighborMo
    
    if 'TABLE_vrf' in output:
        if isinstance(output['TABLE_vrf']['ROW_vrf'],list):
            for vrf in output['TABLE_vrf']['ROW_vrf']:
                mos.extend(parseVrf(vrf))
        else:
            mos.extend(parseVrf(output['TABLE_vrf']['ROW_vrf']))
    return mos
