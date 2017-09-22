from mcpi import minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()
print("x", pos.x)
print("y", pos.y)
print("z", pos.z)

x = 13
y = 5
z = 13
mc.player.setPos(x, y, z)
