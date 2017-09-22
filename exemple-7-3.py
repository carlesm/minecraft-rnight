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
mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

while True:
    for blockhit in mc.player.pollProjectileHits():
        pos = blockhit.pos
        mc.player.setPos(pos.x, pos.y, pos.z)

    time.sleep(0.2)
