#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SimpleTreeTopo(Topo):
    def build(self):
        # Core switch
        core = self.addSwitch('c1')

        # Aggregation switches
        agg1 = self.addSwitch('a1')
        agg2 = self.addSwitch('a2')

        # Edge switches
        edge1 = self.addSwitch('e1')
        edge2 = self.addSwitch('e2')
        edge3 = self.addSwitch('e3')
        edge4 = self.addSwitch('e4')

        # Hosts
        hosts = []
        for i in range(1, 9):
            host = self.addHost(f'h{i}')
            hosts.append(host)

        # Connect core to aggregation
        self.addLink(core, agg1)
        self.addLink(core, agg2)

        # Connect aggregation to edge
        self.addLink(agg1, edge1)
        self.addLink(agg1, edge2)
        self.addLink(agg2, edge3)
        self.addLink(agg2, edge4)

        # Connect edge to hosts
        for i in range(2):
            self.addLink(edge1, hosts[i])      # h1, h2
            self.addLink(edge2, hosts[i+2])    # h3, h4
            self.addLink(edge3, hosts[i+4])    # h5, h6
            self.addLink(edge4, hosts[i+6])    # h7, h8

def run():
    topo = SimpleTreeTopo()
    net = Mininet(topo)
    net.start()
    print("Dumping host connections:")
    dumpNodeConnections(net.hosts)
    print("Testing connectivity:")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
