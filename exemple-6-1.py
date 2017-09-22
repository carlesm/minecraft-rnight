from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()

turtle = MinecraftTurtle(mc, pos)
turtle.speed(10)
for step in range(0, 100):
    turtle.right(4)
    turtle.forward(2)
