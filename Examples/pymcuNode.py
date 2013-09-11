##################################################################
#   
#   pyMCU Maya Node
#	Read analog values and output as Maya Channels
#
##################################################################
# import maya
# maya.cmds.loadPlugin("pymcuNode.py") # Change path to pymcuNode.py to your file location
# maya.cmds.createNode("pymcuNode")
# maya.cmds.connectAttr('time1.outTime', 'pymcuNode1.input', force=True )


import pymcu, sys

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "pymcuNode"

pymcuNodeId = OpenMaya.MTypeId(0x87333)

# Node definition
class pymcuNode(OpenMayaMPx.MPxNode):
	# class variables
	input = OpenMaya.MObject() # Used for time input value
	outputA1 = OpenMaya.MObject()
        outputA2 = OpenMaya.MObject()
        outputA3 = OpenMaya.MObject()
        outputA4 = OpenMaya.MObject()
        outputA5 = OpenMaya.MObject()
        outputA6 = OpenMaya.MObject()
        readA1 = OpenMaya.MObject()
        readA2 = OpenMaya.MObject()
        readA3 = OpenMaya.MObject()
        readA4 = OpenMaya.MObject()
        readA5 = OpenMaya.MObject()
        readA6 = OpenMaya.MObject()
	mb = pymcu.mcuModule()
	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)
	def compute(self,plug,dataBlock):
		if ( plug ):
			dataHandle = dataBlock.inputValue( pymcuNode.input )
			inputFloat = dataHandle.asFloat()
                        readHandle1 = dataBlock.inputValue( pymcuNode.readA1 )
                        read1 = readHandle1.asBool()
                        readHandle2 = dataBlock.inputValue( pymcuNode.readA2 )
                        read2 = readHandle2.asBool()
                        readHandle3 = dataBlock.inputValue( pymcuNode.readA3 )
                        read3 = readHandle3.asBool()
                        readHandle4 = dataBlock.inputValue( pymcuNode.readA4 )
                        read4 = readHandle4.asBool()
                        readHandle5 = dataBlock.inputValue( pymcuNode.readA5 )
                        read5 = readHandle5.asBool()
                        readHandle6 = dataBlock.inputValue( pymcuNode.readA6 )
                        read6 = readHandle6.asBool()
			outputHandle1 = dataBlock.outputValue( pymcuNode.outputA1 )
                        outputHandle2 = dataBlock.outputValue( pymcuNode.outputA2 )
                        outputHandle3 = dataBlock.outputValue( pymcuNode.outputA3 )
                        outputHandle4 = dataBlock.outputValue( pymcuNode.outputA4 )
                        outputHandle5 = dataBlock.outputValue( pymcuNode.outputA5 )
                        outputHandle6 = dataBlock.outputValue( pymcuNode.outputA6 )
                        if read1 == True:
                            result = pymcuNode.mb.analogRead(1)
                            outputHandle1.setFloat( result )
                        if read2 == True:
                            result = pymcuNode.mb.analogRead(2)
                            outputHandle2.setFloat( result )
                        if read3 == True:
                            result = pymcuNode.mb.analogRead(3)
                            outputHandle3.setFloat( result )
                        if read4 == True:
                            result = pymcuNode.mb.analogRead(4)
                            outputHandle4.setFloat( result )
                        if read5 == True:
                            result = pymcuNode.mb.analogRead(5)
                            outputHandle5.setFloat( result )
                        if read6 == True:
                            result = pymcuNode.mb.analogRead(6)
                            outputHandle6.setFloat( result )

                        dataBlock.setClean( plug )

		return OpenMaya.kUnknownParameter

# creator
def nodeCreator():
        print 'start node creator'
	return OpenMayaMPx.asMPxPtr( pymcuNode() )

# initializer
def nodeInitializer():
	# input
	nAttr = OpenMaya.MFnNumericAttribute()
	pymcuNode.input = nAttr.create( "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(1)
	# output
	nAttr = OpenMaya.MFnNumericAttribute()
	pymcuNode.outputA1 = nAttr.create( "outputA1", "outA1", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
	pymcuNode.outputA2 = nAttr.create( "outputA2", "outA2", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
	pymcuNode.outputA3 = nAttr.create( "outputA3", "outA3", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
	pymcuNode.outputA4 = nAttr.create( "outputA4", "outA4", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
	pymcuNode.outputA5 = nAttr.create( "outputA5", "outA5", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
	pymcuNode.outputA6 = nAttr.create( "outputA6", "outA6", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        pymcuNode.readA1 = nAttr.create("readA1", "RA1", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
        pymcuNode.readA2 = nAttr.create("readA2", "RA2", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
        pymcuNode.readA3 = nAttr.create("readA3", "RA3", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
        pymcuNode.readA4 = nAttr.create("readA4", "RA4", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
        pymcuNode.readA5 = nAttr.create("readA5", "RA5", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
        pymcuNode.readA6 = nAttr.create("readA6", "RA6", OpenMaya.MFnNumericData.kBoolean, False)
	nAttr.setStorable(True)
	nAttr.setWritable(True)
        nAttr.setKeyable(True)
        nAttr.setHidden(False)
	# add attributes
	pymcuNode.addAttribute( pymcuNode.input )
	pymcuNode.addAttribute( pymcuNode.outputA1 )
        pymcuNode.addAttribute( pymcuNode.outputA2 )
        pymcuNode.addAttribute( pymcuNode.outputA3 )
        pymcuNode.addAttribute( pymcuNode.outputA4 )
        pymcuNode.addAttribute( pymcuNode.outputA5 )
        pymcuNode.addAttribute( pymcuNode.outputA6 )
        pymcuNode.addAttribute( pymcuNode.readA1 )
        pymcuNode.addAttribute( pymcuNode.readA2 )
        pymcuNode.addAttribute( pymcuNode.readA3 )
        pymcuNode.addAttribute( pymcuNode.readA4 )
        pymcuNode.addAttribute( pymcuNode.readA5 )
        pymcuNode.addAttribute( pymcuNode.readA6 )
	pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA1 )
        pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA2 )
        pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA3 )
        pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA4 )
        pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA5 )
        pymcuNode.attributeAffects( pymcuNode.input, pymcuNode.outputA6 )
        pymcuNode.attributeAffects( pymcuNode.readA1, pymcuNode.outputA1 )
        pymcuNode.attributeAffects( pymcuNode.readA2, pymcuNode.outputA2 )
        pymcuNode.attributeAffects( pymcuNode.readA3, pymcuNode.outputA3 )
        pymcuNode.attributeAffects( pymcuNode.readA4, pymcuNode.outputA4 )
        pymcuNode.attributeAffects( pymcuNode.readA5, pymcuNode.outputA5 )
        pymcuNode.attributeAffects( pymcuNode.readA6, pymcuNode.outputA6 )
	
# initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerNode( kPluginNodeTypeName, pymcuNodeId, nodeCreator, nodeInitializer )
	except:
		sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
		raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode( pymcuNodeId )
	except:
		sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeTypeName )
		raise
	
