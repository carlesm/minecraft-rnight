from mcpi import minecraft
mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

pos = mc.player.getTilePos()
print("x", pos.x)
print("y", pos.y)
print("z", pos.z)

id_pedra = 1
mc.setBlock(pos.x+4, pos.y, pos.z+4, id_pedra)
