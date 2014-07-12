# coding:gbk

def heuristicValue(node):
	return 1
	
def alphabeta(node, depth, alpha, beta, player):
	if depth == 0:
		return heuristicValue(node)
		
	if player == MAX:
		