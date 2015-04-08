#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

from common import Field


class MinmaxAgent(object):
    def __init__(self, symbol=Field.Circle, opponent_symbol=Field.Cross):
        self.symbol = symbol
        self.opponent_symbol = opponent_symbol

    def make_move(self, state, game):
        """
        Selects action to make in given state. Assumes max player.
        :type state: tictactoe.State
        :type game: tictactoe.TicTacToe
        :return: action to take
        """
        score, move = self.max(state, game)
        return move

    def min(self, state, game):
        """
        Processes min-node.
        :type state: tictactoe.State
        :type game: tictactoe.TicTacToe
        :return: tuple, node value, action taken
        """
        # get legal moves for given state
        legal_moves = game.get_legal_moves(state, self.opponent_symbol)
        # compute score for current state
        state_score = self.score(state, game)
        # if state is unknown (None), continue. Return score otherwise.
        if state_score is not None:
            return state_score, None

        children = []
        # for every legal move
        for move in legal_moves:
            # get state after executing action
            next_state = game.apply_move(state, move)
            # get value of child node (for children of min node, it is a maximum).
            # action is irrelevant
            value, dumb = self.max(next_state, game)
            children.append((value, move))

        # select minimal successor
        return min(children)

    # as min
    def max(self, state, game):
        legal_moves = game.get_legal_moves(state, self.symbol)
        state_score = self.score(state, game)
        if state_score is not None:
            return state_score, None

        children = []
        for move in legal_moves:
            next_state = game.apply_move(state, move)
            value, dumb = self.min(next_state, game)
            children.append((value, move))

        return max(children)

    def score(self, state, game):
        """
        Computes state score.
        :type state: tictactoe.State
        :type game: tictactoe.TicTacToe
        :return: Score value, None if state is not terminal. (Is not leaf in tree)
        """
        if game.has_won(state, self.symbol):
            return 1
        elif game.has_lose(state, self.symbol):
            return -1
        elif game.is_terminal(state):
            return 0
        else:
            return None
