import pymem

pm = pymem.Pymem("ac_client.exe")
local_player = pm.read_int(pm.base_address + 0x17B0B8)

while(1):
    pm.write_float(local_player + 0x0C, 7.5)