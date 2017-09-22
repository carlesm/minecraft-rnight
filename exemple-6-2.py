from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getTilePos()
pos.y = pos.y + 10
turtle = MinecraftTurtle(mc, pos)
turtle.penblock(block.FENCE.id)
turtle.speed(10)
turtle.fly()
for step in range(0, 4):
    turtle.forward(10)
    turtle.right(90)
