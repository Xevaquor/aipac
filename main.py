#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we draw text in Russian azbuka.

author: Jan Bodnar
website: zetcode.com
last edited: September 2015
"""

import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QKeyEvent
from layout import Layout, Tile
from pacman import PacmanGame, PacmanGameState
from HumanAgent import HumanAgent
from StopAgent import StopAgent

TILE_SIZE = 20

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.keyboard_state = {'North' : False, 'South' : False, 'West' : False, 'East' : False, 'Stop' : False}

        self.agents = [HumanAgent(0), StopAgent(1)]
        self.layout = Layout()
        self.layout.load_from_file("test.lay")
        self.colors = {Tile.Empty: QBrush(QColor(26,26,26)),
                       Tile.Wall: QBrush(QColor(12,12,225)),
                       Tile.Start: QBrush(QColor(255,255,0))}

        self.game = PacmanGame(self.layout)
        self.current_game_state = self.game.get_initial_game_state()

        self.timer = QBasicTimer()

        self.timer.start(500, self)

    def timerEvent(self, event):

        for i in range(2):
            agent = self.agents[i]
            move = agent.make_decision(self.current_game_state, self.game, self.keyboard_state)
            assert move in self.game.get_legal_moves(self.current_game_state)
            self.current_game_state = self.game.apply_move(self.current_game_state, move, i)


        #move = self.pacman_agent.make_decision(self.current_game_state, self.game, self.keyboard_state)

        # assert that returned move is valid

        #self.current_game_state = self.game.apply_move(self.current_game_state, move, 0)

        self.repaint()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == 0x01000013:
            self.keyboard_state['North'] = True
        elif event.key() == 0x01000015:
            self.keyboard_state['South'] = True
        elif event.key() == 0x01000012:
            self.keyboard_state['West'] = True
        elif event.key() == 0x01000014:
            self.keyboard_state['East'] = True

    def keyReleaseEvent(self, event : QKeyEvent):
        if event.key() == 0x01000013:
            self.keyboard_state['North'] = False
        elif event.key() == 0x01000015:
            self.keyboard_state['South'] = False
        elif event.key() == 0x01000012:
            self.keyboard_state['West'] = False
        elif event.key() == 0x01000014:
            self.keyboard_state['East'] = False


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen (QPen(QColor(0,0,0,0)))
        ysize, xsize = self.layout.shape
        canvas = self.contentsRect()
        for y in range(ysize):
            for x in range(xsize):
                qp.setBrush(self.colors[self.layout.grid[y][x]])
                qp.drawRect(TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE)
                #Color(rgb=self.colors[self.layout.grid[y][x]])
                #Rectangle(pos=(TILE_SIZE * x, TILE_SIZE * y), size=(TILE_SIZE, TILE_SIZE))

        pac_x = self.current_game_state.agents[0].position[0] * TILE_SIZE
        pac_y = self.current_game_state.agents[0].position[1] * TILE_SIZE
        qp.setBrush(QBrush(QColor(255,255,0)))
        qp.drawEllipse(pac_x, pac_y, TILE_SIZE, TILE_SIZE)

        for g in self.current_game_state.agents[1:]:
            g_x = g.position[0] * TILE_SIZE
            g_y = g.position[1] * TILE_SIZE
            qp.setBrush(QBrush(QColor(255,0,0)))
            qp.drawEllipse(g_x, g_y, TILE_SIZE, TILE_SIZE)

        for y in range(ysize):
            for x in range(xsize):
                if self.current_game_state.food[y][x]:
                    qp.setBrush(QBrush(QColor(255,255,255)))
                    qp.drawEllipse(x * TILE_SIZE + TILE_SIZE / 2,
                                 y * TILE_SIZE + TILE_SIZE / 2,
                            TILE_SIZE / 4, TILE_SIZE / 4)

        qp.end()


    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())