# -*-coding:utf-8 -*-
#
# Import the libraries we need

from PUC_lib import base_Test
from PUC_lib import Mytool
from PUC_lib import platform_Test

__verison__ = "LDF1.0"

class auto_Test(base_Test, Mytool,platform_Test ):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

# class auto_Test(Mytool):
# 	ROBOT_LIBRARY_SCOPE = 'GLOBAL'


#class auto_Test(platform_Test):
#    ROBOT_LIBRARY_SCOPE = 'GLOBAL'