#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

from layout import *
from copy import deepcopy

Moves = {
    'North' : (0, -1),
    'South' : (0, 1),
    'East': (1, 0),
    'West' : (-1, 0),
    'Stop' : (0, 0)
}


class AgentStatus(object):
    def __init__(self, pos = (0,0), scared = False):
        self.position = pos
        self.is_scared = scared


class PacmanGameState(object):
    def __init__(self, food):
        # 0 - pacman
        # >0 - ghost
        self.agents = [None, None]
        self.power_pellets = []
        self.food = deepcopy(food)


class PacmanGame(object):
    def __init__(self, lay):
        self.layout = lay

    def get_initial_game_state(self):
        gs = PacmanGameState(self.layout.food)
        gs.agents[0] = AgentStatus(pos=(3, 1), scared=False)
        gs.agents[1] = AgentStatus(pos=(2, 1), scared=False)
        return gs

    def get_legal_moves(self, state, agent_index=0):
        if agent_index != 0:
            raise Exception("Not implemented!")

        legal_moves = []

        x, y = state.agents[agent_index].position
        for m, d in Moves.items():
            dx, dy = d
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < self.layout.cols and ny >= 0 and ny < self.layout.rows:
                if self.layout.grid[ny][nx] != Tile.Wall:
                    legal_moves.append(m)

        return legal_moves


    def apply_move(self, state, move, agent_index=0):
        # assert move is legal
        # only move so far
        dx, dy = Moves[move]

        s = deepcopy(state)
        s.agents[agent_index].position =( s.agents[agent_index].position[0] +  dx,
        s.agents[agent_index].position[1] + dy)

        # eat food
        if agent_index == 0:
            x, y = s.agents[agent_index].position
            s.food[y][x] = False

        return s


    def is_terminate(self, state):
        pass

    def pacman_won(self, state):
        pass

    def pacman_lose(self, state):
        pass

    def get_score(self, state):
        pass



