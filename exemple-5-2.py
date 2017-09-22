from mcpi import minecraft
mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

pos = mc.player.getTilePos()

pos.x = pos.x - 10
pos.y = pos.y - 10
pos.z = pos.z - 10

id_pedra = 2

for i in range(0,20):
    mc.setBlock(pos.x+i, pos.y+10, pos.z, id_pedra)
    mc.setBlock(pos.x, pos.y+10, pos.z+i, id_pedra)
    mc.setBlock(pos.x+19, pos.y+10, pos.z+i, id_pedra)
    mc.setBlock(pos.x+i, pos.y+10, pos.z+19, id_pedra)
