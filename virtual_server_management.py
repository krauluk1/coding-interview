""" 
Approximate sequence of coding challenge:
1. Task is explained orally 
2. Expectations are clarified
3. Own planning and coding. Only answers to questions come.

Brief summary of my task:
1. How many servers do I need to buy to accommodate all my virtual servers?
-> Input: Offer data, Virtual Server data
-> Output: Quantity
=> Default: Use first fit algorithm 
=> Madatory: Use unit testing to find out if your code works (here pytest)
"""

import pytest

class VirtualServer(object):
    def __init__(self, name, cpu, bandwidth, ram) -> None:
        super().__init__()
        self.cpu = int(cpu)
        self.bandwidth = int(bandwidth)
        self.ram = int(ram)
        self.name = name

    def set_cpu(self, val):
        self.cpu = val

    def set_bandwidth(self, val):
        self.bandwidth = val

    def set_ram(self, val):
        self.ram = val

    def get_cpu(self):
        return self.cpu
    
    def get_bandwidth(self):
        return self.bandwidth

    def get_ram(self):
        return self.ram

    def get_name(self):
        return self.name

class InsufficientServerSize(Exception):
    pass

class Server(VirtualServer):
    def __init__(self, name, cpu, bandwidth, ram) -> None:
        super().__init__(name, cpu, bandwidth, ram)
        self.used_server = []

    def add_virtual_machine_to_server(self, vr):
        if(self.get_cpu() - vr.get_cpu() >= 0 and self.get_bandwidth() - vr.get_bandwidth() >= 0 and self.get_ram() - vr.get_ram() >= 0):
            self.used_server.append(vr)
            self.set_cpu(self.get_cpu() - vr.get_cpu())
            self.set_bandwidth(self.get_bandwidth() - vr.get_bandwidth())
            self.set_ram(self.get_ram() - vr.get_ram())
            return True
        return False

    def get_used_server(self):
        return self.used_server

class CalculateNumber(object):
    def __init__(self) -> None:
        super().__init__()
        self.offer = []
        self.server = []
        self.virtual_machines = []

    def add_virtual_machine(self, name, cpu, bandwidth, ram):
        data = VirtualServer(name, cpu, bandwidth, ram)
        self.virtual_machines.append(data)

    def add_offer(self, name, cpu, bandwidth, ram):
        data = VirtualServer(name, cpu, bandwidth, ram)
        self.offer.append(data)

    def add_server(self, name, cpu, bandwidth, ram):
        data = Server(name, cpu, bandwidth, ram)
        self.server.append(data)

    def calculate_number(self):
        self.add_server("Server", self.offer[0].get_cpu(), self.offer[0].get_bandwidth(), self.offer[0].get_ram())
        
        for vr in self.virtual_machines:
            used = False
            for sr in self.server:
                if(sr.add_virtual_machine_to_server(vr)):
                    used = True
                    break
            if(not used):
                self.add_server("Server", self.offer[0].get_cpu(), self.offer[0].get_bandwidth(), self.offer[0].get_ram())
                if(not self.server[-1].add_virtual_machine_to_server(vr)):
                    raise InsufficientServerSize('The server is smaller than the virtual server')
            
    def get_number_vr(self):
        return str(len(self.server))

class Tester(object):        
    def test_virtual_server(self):
        vs1 = VirtualServer("Virtual Server 1", 22, 32, 32)
        assert vs1.get_name() == "Virtual Server 1"
        assert vs1.get_cpu() == 22
        assert vs1.get_bandwidth() == 32
        assert vs1.get_ram() == 32

    def test_server(self):
        sv1 = Server("Server 1", 22,32,32)
        assert sv1.get_name() == "Server 1"
        assert sv1.get_cpu() == 22
        assert sv1.get_bandwidth() == 32
        assert sv1.get_ram() == 32

    def test_calculation(self):
        c1 = CalculateNumber()
        c1.add_offer("Benz", 42, 23 ,43)
        c1.add_virtual_machine("V1", 22,21,23)
        c1.add_virtual_machine("V2", 2,1,2)
        c1.add_virtual_machine("V3", 23,21,32)
        c1.calculate_number()
        assert c1.get_number_vr() != 2

