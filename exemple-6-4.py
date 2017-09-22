from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

pos = mc.player.getPos()

turtle = MinecraftTurtle(mc, pos)
turtle.speed(0)
turtle.setheading(90)
NumberOfSides = 5
Angle = 360 / NumberOfSides
SideLength = 20
WoolColour = 0

for count in range(24):
    for side in range(NumberOfSides):
        turtle.forward(SideLength)
        turtle.right(Angle)
    turtle.right(15)
    WoolColour += 1
    if WoolColour > 15:
        WoolColour = 0
    turtle.penblock(block.WOOL.id, WoolColour)
