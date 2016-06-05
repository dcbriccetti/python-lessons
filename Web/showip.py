# Uses https://pypi.python.org/pypi/netifaces

import netifaces
for interface_name in netifaces.interfaces():
    addrs_for_iface = netifaces.ifaddresses(interface_name)
    inet_addrs = addrs_for_iface.get(netifaces.AF_INET)
    if inet_addrs:
        for addr in inet_addrs:
            ip_address = addr['addr']
            if ip_address != '127.0.0.1':
                print(interface_name, ip_address)
