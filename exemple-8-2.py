# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Minecraft Turtle Example
# Ported from the scratch turtle project in "Adventures in Raspberry Pi"
import time
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

while True:
    for chatpost in mc.player.pollChatPosts():
        if chatpost.message == "aigua":
            pos = mc.player.getPos()
            mc.setBlock(pos.x, pos.y+3, pos.z, block.WATER.id)
        elif chatpost.message == "foc":
            pos = mc.player.getPos()
            mc.setBlock(pos.x+5, pos.y+1, pos.z+5, block.LAVA.id)


    time.sleep(0.2)
