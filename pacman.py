#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

from lyout import *

class AgentStatus(object):
    def __init__(self):
        self.position = (0,0)
        self.is_scared = False


class PacmanGameState(object):
    def __init__(self):
        # 0 - pacman
        # >0 - ghost
        self.agents = [None, None]
        self.power_pellets = []
        self.food = None


class PacmanGame(object):
    def __init__(self):
        pass

    def get_legal_moves(self, state, agent_index=0):
        pass

    def apply_move(self, state, move, agent_index=0:
        pass

    def is_terminate(self, state):
        pass

    def pacman_won(self, state):
        pass

    def pacman_lose(self, state):
        pass

    def get_score(self, state):
        pass



