# works with pymcuNode.py and Autodesk Maya

import maya
 
maya.cmds.loadPlugin("c:/temp/pymcuNode.py")   # Change the path to where you put the pymcuNode.py file
maya.cmds.createNode('pymcuNode')
maya.cmds.connectAttr('time1.outTime', 'pymcuNode1.input', force=True )
maya.cmds.createNode('directionalLight')
maya.cmds.createNode('multiplyDivide')
maya.cmds.setAttr("multiplyDivide1.operation", 2)
maya.cmds.setAttr("multiplyDivide1.input2X", 10)
maya.cmds.connectAttr('pymcuNode1.outputA1', 'multiplyDivide1.input1X', force=True )
maya.cmds.connectAttr('multiplyDivide1.outputX', 'directionalLight1.intensity', force=True )
maya.cmds.polySphere(sx=20, sy=20, r=7, ax=[0,1,0], cuv=2, ch=1)
maya.cmds.connectAttr('pymcuNode1.outputA2','pSphere1.translateX', force=True)
maya.cmds.setAttr('pymcuNode1.readA1', True)
maya.cmds.setAttr('pymcuNode1.readA2', True)
