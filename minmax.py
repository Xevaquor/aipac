#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

from common import Field


class MinmaxAgent(object):
    def __init__(self, symbol=Field.Circle, opponent_symbol=Field.Cross):
        self.symbol = symbol
        self.opponent_symbol = opponent_symbol
        pass

    def make_move(self, state, game):
        score, move = self.max(state, game)
        return move

    def min(self, state, game):
        legal_moves = game.get_legal_moves(state, self.opponent_symbol)
        state_score = self.score(state, game)
        if state_score is not None:
            return state_score, None

        children = []
        for move in legal_moves:
            next_state = game.apply_move(state, move)
            value, dumb = self.max(next_state, game)
            children.append((value, move))

        return min(children)

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
        if game.has_won(state, self.symbol):
            return 1
        elif game.has_lose(state, self.symbol):
            return -1
        elif game.is_terminal(state):
            return 0
        else:
            return None
