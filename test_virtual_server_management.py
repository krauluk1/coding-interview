""" 
Testing part of virtual_server_management.py
"""
from virtual_server_management import VirtualServer, Server, CalculateNumber

class TestVirtualServerManagement(object):        
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
        assert c1.get_number_vr() == 2