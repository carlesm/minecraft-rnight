from mcpi import minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()
print("x", pos.x)
print("y", pos.y)
print("z", pos.z)
mc.postToChat("Estas a "+str(pos.x)+","+str(pos.y)+","+str(pos.z))
