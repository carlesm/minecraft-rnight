from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

# Connectar servidor minecraft
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

# Posicio
pos = mc.player.getPos()

# Crear Tortuga
turtle = MinecraftTurtle(mc, pos)

turtle.speed(0)
turtle.penblock(block.WOOL.id, 14)
S = 50
for j in range(0, 20):
    turtle.up(j * 10)
    turtle.forward(S)

    turtle.left(90)
    turtle.down(j * 10)
    turtle.forward(S)

    turtle.left(90)
    turtle.down(j * 10)
    turtle.forward(S)

    turtle.left(90)
    turtle.up(j * 10)
    turtle.forward(S)
    turtle.left(90)

    turtle.left(10)
    S = 0.9 * S
