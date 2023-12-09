import numpy as np
import random

class MCTSNode:
    def __init__(self, state, player, move=None, parent=None):
        self.player = player
        self.state = state
        self.move = move
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

def ucb_score(node):
    if node.visits == 0:
        return float('inf')
    return (node.wins / node.visits) + 1.41 * np.sqrt(np.log(node.parent.visits) / node.visits)

def select(node, activeBoardRow, activeBoardCol):
    while not node.state.is_terminal():
        if len(node.children) < len(node.state.get_legal_moves()):
            return expand(node, activeBoardRow, activeBoardCol)
        node = max(node.children, key=ucb_score, default=None)
    return node

def expand(node, activeBoardRow, activeBoardCol):
    legal_moves = node.state.get_legal_moves()
    legal_moves = [move for move in legal_moves if move[2] == activeBoardRow and move[3] == activeBoardCol]
    if not legal_moves:
        legal_moves = node.state.get_legal_moves()
    untried_moves = [move for move in legal_moves if move not in [child.move for child in node.children]]

    if untried_moves:
        move = random.choice(untried_moves)
        new_state = node.state.copy()
        new_state.apply_move(move, node.player, True)
        new_node = MCTSNode(new_state, node.player, move, parent=node)
        node.children.append(new_node)
        return new_node
    else:
        return max(node.children, key=ucb_score, default=None)

def mtcsPlayerMove(player):
    player = 3 - player
    return player

def simulate(node):
    state = node.state.copy()
    while not state.is_terminal():
        legal_moves = state.get_legal_moves()
        move = random.choice(legal_moves)
        state = state.perform_move(move)
    return state.final_state()

def backpropagate(node, result):
    while node is not None:
        node.visits += 1
        if mtcsPlayerMove(node.player) == result:
            node.wins += 1
        node = node.parent

def mcts(wide_board, activeBoardRow, activeBoardCol, player, iterations=1000):
    root = MCTSNode(wide_board.copy(), player)

    for _ in range(iterations):
        node = select(root, activeBoardRow, activeBoardCol)
        if not node.state.is_terminal():
            result = node.state.final_state()
        else:
            node_expanded = expand(node, activeBoardRow, activeBoardCol)
            result = simulate(node_expanded)
        backpropagate(node, result)

    best_child = max(root.children, key=lambda x: x.visits)
    #print(best_child.move)
    return best_child.move, best_child.visits
