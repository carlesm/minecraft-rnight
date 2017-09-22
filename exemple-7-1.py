import time
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create(address="minecraft.lliure.cat", name="test1")

while True:
    for blockhit in mc.player.pollBlockHits():
        pos = blockhit.pos
        gold_block_id = 41
        mc.setBlock(pos.x, pos.y, pos.z, gold_block_id)
    time.sleep(1)
