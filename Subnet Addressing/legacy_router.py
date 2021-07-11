# ===================================================================
# Legacy Router - Fixed
# Roland Bernard, Jordan Bienz, Christopher Boyd, Miguel Solis
# -------------------------------------------------------------------
#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    # Define the mininet object
    net = Mininet( topo=None,
                   build=False,
                   # IP address for router
                   ipBase='10.0.0.1/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    # Changed node IP to ipBase. Router designated 10.0.0.1
    r1 = net.addHost('r1', cls=Node, ip='10.0.0.1/8')
    # IP forwarding set up on router
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '*** Add hosts\n')
    # Set host IPs to utilize two different subnets
    # Default route was not set. Set to link IPs
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.100/8', defaultRoute='via 10.0.0.1')
    h2 = net.addHost('h2', cls=Host, ip='192.168.1.100/24', defaultRoute='via 192.168.1.1')
    
    info( '*** Add links\n')
    # Links contained no assigned IPs or interface names, created IPs and subnets
    # eth0 subnet: 10.0.0.0/8 - eth1 subnet - 192.168.1.1/24
    net.addLink(h1, r1, intfName2='r1-eth0', params2={ 'ip' : '10.0.0.0/8' })
    net.addLink(h2, r1, intfName2='r1-eth1', params2={ 'ip' : '192.168.1.1/24'})
    
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    # Code below this point was not changed
    info( '*** Starting switches\n')

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

