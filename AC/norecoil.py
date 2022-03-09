from threading import local
import pymem

recoil = 0x

pm = pymem.Pymem("ac_client.exe")
local_player = pm.read_int(pm.base_address + 0x17B0B8)

while(1):
    status = pm.read_int(local_player + recoil)
    if status == 981668463:
        pm.write_int(local_player + recoil, 0)
    else:
        pass