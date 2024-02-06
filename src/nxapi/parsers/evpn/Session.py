from nxapi.parsers.common import moParser
'''
output:
TABLE_neighbor
  ROW_neighbor:list
      neighbor: 10.2.0.4
      remoteas: 100
      link: ibgp
      index: 3
      version: 4
      remote-id: 10.2.0.4
      prevstate: OpenConfirm
      state: Established
      up: true
      vrf: default
      elapsedtime: P10DT22H38M22S
      sourceif: loopback0
      ttlsecurity: false
      passiveonly: false
      localas-inactive: false
      remove-privateas: false
      gshut-activate: false
      lastread: PT10S
      holdtime: 180
      keepalivetime: 60
      lastwrite: PT4S
      keepalive: 0
      msgrecvd: 18605
      notificationsrcvd: 0
      recvbufbytesinq: 0
      msgsent: 16884
      notificationssent: 0
      sentbytesoutstanding: 0
      sentbytespacked: 0
      enhancederr: On
      discardattrs: 0
      connsestablished: 1
      connsdropped: 0
      resetreason: No error
      errlensnt: 0
      errvalsnt: 0
      rstmajsnt: 0
      rstminsnt: 0
      peerresetreason: No error
      errlenrcvd: 0
      errvalrcvd: 0
      rstmajrcvd: 0
      rstminrcvd: 0
      capsnegotiated: false
      capmpadvertised: true
      caprefreshadvertised: true
      capgrdynamicadvertised: true
      capmprecvd: true
      caprefreshrecvd: true
      capgrdynamicrecvd: true
      capolddynamicadvertised: true
      capolddynamicrecvd: true
      caprradvertised: true
      caprrrecvd: true
      capoldrradvertised: true
      capoldrrrecvd: true
      capas4advertised: true
      capas4recvd: true
      capgradvertised: true
      capgrrecvd: true
      grrestarttime: 120
      grstaletime: 300
      grrecvdrestarttime: 120
      capextendednhadvertised: true
      capextendednhrecvd: true
      epe: false
      firstkeepalive: false
      openssent: 1
      opensrecvd: 1
      updatessent: 3113
      updatesrecvd: 2869
      keepalivesent: 15729
      keepaliverecvd: 15733
      rtrefreshsent: 12
      rtrefreshrecvd: 0
      capabilitiessent: 2
      capabilitiesrecvd: 2
      bytessent: 626790
      bytesrecvd: 606003
      localaddr: 10.2.0.3
      localport: 179
      remoteaddr: 10.2.0.4
      remoteport: 57590
      fd: 74
      TABLE_capextendednhaf
        ROW_capextendednhaf:list
            capextendednh-afi: 1
            TABLE_capextendednhsaf
              ROW_capextendednhsaf
                capextendednh-safi: 1
                capextendednh-af-name: IPv4 Unicast
      TABLE_af
        ROW_af
          af-afi: 25
          TABLE_saf
            ROW_saf
              af-safi: 70
              af-advertised: true
              af-recvd: true
              af-name: L2VPN EVPN
      TABLE_peraf
        ROW_peraf
          per-afi: 25
          TABLE_persaf
            ROW_persaf
              per-safi: 70
              per-af-name: L2VPN EVPN
              tableversion: 8541
              neighbortableversion: 8541
              pfxrecvd: 10
              pathsrecvd: 10
              pfxbytes: 2520
              pfxtreataswithdrawn: 0
              pfxsent: 24
              pathssent: 24
              insoftreconfigallowed: false
              sendcommunity: true
              sendextcommunity: true
              thirdpartynexthop: true
              asoverride: false
              peerascheckdisabled: false
              rrconfigured: false
              defaultoriginate: false
              lasteorrecvtime: P1DT18M59S
              lasteorsenttime: P8DT22H22M14S
              firstconvgtime: P10DT23H27M27S
              pfxsentfirsteor: 0
      TABLE_graf
        ROW_graf
          gr-afi: 25
          TABLE_grsaf
            ROW_grsaf
              gr-safi: 70
              gr-af-name: L2VPN EVPN
              gr-adv: true
              gr-recv: true
              gr-fwd: false
'''

def createMo(output):
    '''
    Parse entire output of 'show bgp l2vpn evpn neighbors' and return a list of mos of class Session
    Also include all the information from the output in the mos
    AF, PeerAF, PerAF, and GRAF information should be present in dictinary form within the mos
    '''
    mos = []
    from nxapi.model.evpn.Session import evpnSession
    if 'TABLE_neighbor' not in output:
        return mos
    if isinstance(output['TABLE_neighbor']['ROW_neighbor'], list):
        for neighbor in output['TABLE_neighbor']['ROW_neighbor']:
            mo = evpnSession()
            moParser(neighbor, mo)
            mos.append(mo)
    else:
        mo = evpnSession()
        moParser(output['TABLE_neighbor']['ROW_neighbor'], mo)
        mos.append(mo)
    return mos

