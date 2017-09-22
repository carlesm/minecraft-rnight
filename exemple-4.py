from mcpi import minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()

id_pedra = 1

for i in range(1,20):
    mc.setBlock(pos.x+i, pos.y, pos.z, id_pedra)
