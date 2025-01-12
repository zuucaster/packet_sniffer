
**Code (packet_sniffer.py)**  
```python
from scapy.all import sniff

# Function to process packets
def packet_callback(packet):
    print(packet.summary())  # Display packet details

print("Starting packet sniffer...")
sniff(prn=packet_callback, count=10)  # Capture 10 packets
