from mcpi import minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()
id_pedra = 1
mc.setBlock(pos.x+4, pos.y, pos.z+4, id_pedra)
