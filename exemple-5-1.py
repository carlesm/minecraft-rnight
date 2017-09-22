from mcpi import minecraft
mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

pos = mc.player.getTilePos()
print("x", pos.x)
print("y", pos.y)
print("z", pos.z)

id_pedra = 1

for i in range(0,20):
    mc.setBlock(pos.x+i, pos.y+10, pos.z, id_pedra)
    mc.setBlock(pos.x, pos.y+10, pos.z+i, id_pedra)
    mc.setBlock(pos.x+19, pos.y+10, pos.z+i, id_pedra)
    mc.setBlock(pos.x+i, pos.y+10, pos.z+19, id_pedra)
