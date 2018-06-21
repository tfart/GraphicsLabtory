"""
Declaration: Copyright (c), by idovelemoen, 2018. All right reserved.
Author: idovelemon[1322600812@qq.com]
Date: 2018-06-21
Brief: Level 0
"""

from sys import *
from host_api import *

LEVEL_COUNT = 0

def main():
    global LEVEL_COUNT
    LEVEL_COUNT = LEVEL_COUNT + 1

    if LEVEL_COUNT == 1:
        DebugPrint("TD Level0 Start\n")

    if LEVEL_COUNT == 2:
        # Create Camera Entity
        camera = EntityCreate()
        EntityAddCameraCom(camera, 0.0, 5.0, 10.0, 0.0, 0.0, 0.0)

        # Create Core Entity
        core = EntityCreate()
        EntityAddTransformCom(core, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(core, "res/model/core/core.obj", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(core, "EntityCoreUpdater")

        # Create Core Rot Entity
        coreRot = EntityCreate()
        EntityAddTransformCom(coreRot, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(coreRot, "res/model/core/coreRot.obj", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(coreRot, "EntityCoreRotUpdater")

        # Create Four Normal Emitter
        backNormalEmitter = EntityCreate()
        EntityAddTransformCom(backNormalEmitter, 0.0, 0.75, 1.8, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(backNormalEmitter, "res/model/emitter/normal_Emitter.obj", 0.0, 0.75, 1.8, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(backNormalEmitter, "EntityNormalEmitterUpdater")

        frontNormalEmitter = EntityCreate()
        EntityAddTransformCom(frontNormalEmitter, 0.0, 0.75, -1.8, 0.0, 180.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(frontNormalEmitter, "res/model/emitter/normal_Emitter.obj", 0.0, 0.75, -1.8, 0.0, 180.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(frontNormalEmitter, "EntityNormalEmitterUpdater")

        leftNormalEmitter = EntityCreate()
        EntityAddTransformCom(leftNormalEmitter, -1.8, 0.75, 0.0, 0.0, -90.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(leftNormalEmitter, "res/model/emitter/normal_Emitter.obj", -1.8, 0.75, 0.0, 0.0, -90.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(leftNormalEmitter, "EntityNormalEmitterUpdater")

        rightNormalEmitter = EntityCreate()
        EntityAddTransformCom(rightNormalEmitter, 1.8, 0.75, 0.0, 0.0, 90.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddRenderCom(rightNormalEmitter, "res/model/emitter/normal_Emitter.obj", 1.8, 0.75, 0.0, 0.0, 90.0, 0.0, 1.0, 1.0, 1.0)
        EntityAddScriptCom(rightNormalEmitter, "EntityNormalEmitterUpdater")        

    if LEVEL_COUNT == 20:
        DebugPrint("TD Level0 Finish\n")