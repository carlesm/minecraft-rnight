from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

pos = mc.player.getTilePos()

turtle = MinecraftTurtle(mc, pos)
turtle.speed(10)
for step in range(0, 20):
    turtle.right(5)
    turtle.forward(2)
