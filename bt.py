import bluetooth

devices = bluetooth.discover_devices(lookup_names = True)

for i in devices:
    print(bluetooth.lookup_name(i))