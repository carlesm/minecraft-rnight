import time
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

while True:
    for blockhit in mc.player.pollProjectileHits():
        pos = blockhit.pos
        mc.player.setPos(pos.x, pos.y, pos.z)

    time.sleep(0.2)
