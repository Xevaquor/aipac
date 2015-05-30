#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

from pacman import *

class HumanAgent(object):
    def __init__(self, agent_index):
        self.agent_index = agent_index


    def make_decision(self, state, game, input_state):
        legal_moves = game.get_legal_moves(state)
        # self.current_game_state = self.game.apply_move(self.current_game_state, random.sample(legal_moves, 1)[0], 0)
        move = 'Stop'
        for m in [x for x in legal_moves if x != 'Stop']:
            if input_state[m]:
                move = m
        assert move is not None

        return move