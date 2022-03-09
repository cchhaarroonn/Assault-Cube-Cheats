import time
import pymem
import keyboard

newHealth = int(input("Enter health number: "))
newRifleAmmo = int(input("Enter rifle ammo: "))
newPistolAmmo = int(input("Enter pistol ammo: "))

pm = pymem.Pymem("ac_client.exe")
local_player = pm.read_int(pm.base_address + 0x17B0B8)
health = pm.read_int(local_player + 0xEC)
rifleAmmo = pm.read_int(local_player + 0x140)
pistolAmmo = pm.read_int(local_player + 0x12C)
currentHeight = pm.read_float(local_player + 0x0C)

print(f"""
Your current status was:

Health: {health}
Rifle ammo: {rifleAmmo}
Pistol ammo: {pistolAmmo}
""")

print(f"""
Your new status is:

Health: {newHealth}
Rifle ammo: {newRifleAmmo}
Pistol ammo: {newPistolAmmo}
""")

while(1):
    pm.write_int(local_player + 0xEC, newHealth)
    pm.write_int(local_player + 0x140, newRifleAmmo)
    pm.write_int(local_player + 0x12C, newPistolAmmo)

    if keyboard.is_pressed("f"):
        pm.write_float(local_player + 0x0C, currentHeight + 3.5)
