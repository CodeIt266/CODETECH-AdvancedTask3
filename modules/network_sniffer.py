from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)
