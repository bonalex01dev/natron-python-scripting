#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 16/07/2019.

from NatronEngine import *
from NatronGui import *


def findEnds(processNodes):
	endNodes = []
	tailNodes = [] 
	headNodes = []
	for currentNode in processNodes:
		inputFound = False
		outputFound = False
		for testNode in processNodes:
			if testNode == currentNode.getInput(0):
				inputFound = True
			if testNode.getInput(0) == currentNode:
				outputFound = True
	if inputFound != True:
		headNodes.append(currentNode)
	if outputFound != True:
		tailNodes.append(currentNode)
	endNodes.append(headNodes)
	endNodes.append(tailNodes)
	return endNodes

def offsetNodes(DirectionUp):
	# get current Natron instance running in memory #
	myApp = natron.getActiveInstance()
	app = natron.getGuiInstance( myApp.getAppID() )

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()
	# check if at least one node has been selected #
	if len(selectedNodes) == 0:
		warning = natron.warningDialog("Warning","Select at least one node.")
	else :
		# check that selection linear shaped
		endNodes = findEnds(selectedNodes)
		if sizeof(endNodes[0]) !=1 or sizeof(endNodes[1]) !=1:
			warning = natron.warningDialog("Warning","Ambiguous structure can't offset nodes.")
		else:
			headNode = endNodes[0][0]
			aboveNode = headNode.getInput(0)
			tailNode = endNodes[1][0]
			
			# search nodes above and below
			belowNodes = []
			app.clearSelection()
			app.selectAllNodes()
			for testNode in app.getSelectedNodes():
				if testNode.getInput(0) = tailNode:
					belowNodes.append(testNode)
			
			# do the actual offset
			if DirectionUp = True and aboveNode != None:
				headNode.disconnectInput(0)
				for currentNode in belowNodes:
					current.disconnectInput(0)

				# add reconnections here
			if directionUp = False:
				if sizeof(belowNodes)=1:
					headNode.disconnectInput(0)
					for currentNode in belowNodes:
						current.disconnectInput(0)

						# add reconnections here
				elif sizeof(belowNodes)>1:
					warning = natron.warningDialog("Warning","Too many downstream nodes. Can't offset nodes.")
