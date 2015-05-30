#!/usr/bin/env python
# coding=utf-8
__author__ = 'Xevaquor'
__license__ = 'MIT'

class StopAgent(object):
    def __init__(self, agent_index):
        pass

    def make_decision(self, state, game, input_state):
        return 'Stop'

