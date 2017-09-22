import time
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create(address="193.144.12.6", name="test1")

while True:
    for chatpost in mc.player.pollChatPosts():
        if chatpost.message == "aigua":
            pos = mc.player.getPos()
            mc.setBlock(pos.x, pos.y+3, pos.z, block.WATER.id)


    time.sleep(0.2)
