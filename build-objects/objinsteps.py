from mcpi.minecraft import *
mc=Minecraft.create()
from time import sleep
import math
from random import randint

#get amunt of steps
steps=int(input("How many steps?"))
#get player position
pos=mc.player.getTilePos()
#random block type
block=randint(1,15)
#set block
mc.setBlock(pos.x+steps,pos.y,pos.z,block)
