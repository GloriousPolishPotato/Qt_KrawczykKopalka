# Klasa QWidgetu gry
#
#   TODO Opis pliku, klas i metod w nim zawieranych
#
#
#  Autorzy: Szymon Krawczyk, Michał Kopałka
#
#  Plik początkowo wygenerowany:
#   -*- coding: utf-8 -*-
#   Form implementation generated from reading ui file 'gameView2.ui'
#
#   Created by: PyQt5 UI code generator 5.15.1
#
#
#           11.11.2020 | Szymon Krawczyk    | Utworzenie
#           12.11.2020 | Szymon Krawczyk    | Rysowanie v1:
#                                           |   Rysowanie bezpośrednio na GameView, usunięcie myCanvas
#                                           |       (prostsze rozwiązanie na chwilę obecną)
#           14.11.2020 | Szymon Krawczyk    | Wyczyszczenie kodu
#           14.11.2020 | Szymon Krawczyk    | Usunięcie metody hardReset na próbę (nie wydaje się potrzebna)
#           14.11.2020 | Szymon Krawczyk    | Dodanie poruszania się węża
#           14.11.2020 | Szymon Krawczyk    | Rysowanie v2: Rysowanie węża i jego ogonu
#           16.11.2020 | Szymon Krawczyk    | Przeniesienie kolorów z klasy Snake tutaj
#           16.11.2020 | Szymon Krawczyk    | Dodanie funkcjonalności 'zawijania' się planszy
#                                           |   (teleportacji z jednej strony na drugą)
#           16.11.2020 | Szymon Krawczyk    | Poprawa błędu krytycznego - wielkość rysowania przy zmianie długości boku
#

#   Legenda oznaczeń wewnątrz macierzy komórek
#       0-puste
#       1-jedzenie
#       2-super jedzenie
#       7-ściana


import sys
from random import randrange

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

from Snake import Snake


class GameView(QWidget):

    # Właściwości

    # Nowy kierunek ruchu
    @property
    def newDirection(self):
        return self._newDirection

    @newDirection.setter
    def newDirection(self, value):
        if value != "N" and value != "E" and value != "W" and value != "S" and value != "":
            raise ValueError
        self._newDirection = value

    # Ilość ruchów na sekundę (szybkość gry) - musi być w przedziale
    @property
    def CPS(self):
        return self._CPS

    @CPS.setter
    def CPS(self, value):
        if value < 1 or value > 10:
            raise ValueError
        self._CPS = value

    # Ilość komórek na ekranie gry (bok) - musi być nieparzysty i w przedziale
    @property
    def cellCount(self):
        return self._cellCount

    @cellCount.setter
    def cellCount(self, value):
        if value % 2 == 0 or value < 11 or value > 41:
            raise ValueError
        self._cellCount = value

    # Opcja - czy generować powerUpy
    @property
    def powerups(self):
        return self._powerups

    @powerups.setter
    def powerups(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._powerups = value

    # Opcja - czy obszar gry ma być otoczony ścianą
    @property
    def closedBox(self):
        return self._closedBox

    @closedBox.setter
    def closedBox(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._closedBox = value

    # Opcja - czy generować losową ścianę w środku gry
    @property
    def randomWall(self):
        return self._randomWall

    @randomWall.setter
    def randomWall(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self._randomWall = value

    def __init__(self):
        super().__init__()

        # Deklaracja pól i wartości domyślne
        self.newDirection = ""
        self.CPS = 2
        self.cellCount = 21
        self.powerups = True
        self.closedBox = True
        self.randomWall = True

        self.gameMatrix = []
        self.paintFlag = True

        self.Python = Snake()
        self.gameOver = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimeout)

        # UI wygenerowane automatycznie
        self.width = 600
        self.height = 800
        self.setFixedSize(self.width, self.height)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 440, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scoreHigh = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.scoreHigh.setFont(font)
        self.scoreHigh.setObjectName("scoreHigh")
        self.verticalLayout_2.addWidget(self.scoreHigh)

        self.scoreCurrent = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.scoreCurrent.setFont(font)
        self.scoreCurrent.setObjectName("scoreCurrent")

        self.verticalLayout_2.addWidget(self.scoreCurrent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # self.myCanvas = QtWidgets.QWidget(self)
        self.cellWidth = int((self.width-100) / self.cellCount)
        self.myCanvasSize = int(self.cellWidth * self.cellCount)
        self.myCanvasPaddingX = (self.width-self.myCanvasSize)/2
        self.myCanvasPaddingY = 100
        # self.myCanvas.setGeometry(QtCore.QRect(int(tempPaddingX), 100, self.myCanvasSize, self.myCanvasSize))
        # self.myCanvas.setObjectName("myCanvas")

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 610, 239, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.arrRight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrRight.setObjectName("arrRight")
        self.arrRight.clicked.connect(self.arrRightClicked)
        self.gridLayout.addWidget(self.arrRight, 1, 2, 1, 1)

        self.arrUp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrUp.setObjectName("arrUp")
        self.arrUp.clicked.connect(self.arrUpClicked)
        self.gridLayout.addWidget(self.arrUp, 0, 1, 1, 1)

        self.arrLeft = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrLeft.setObjectName("arrLeft")
        self.arrLeft.clicked.connect(self.arrLeftClicked)
        self.gridLayout.addWidget(self.arrLeft, 1, 0, 1, 1)

        self.arrDown = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.arrDown.setObjectName("arrDown")
        self.arrDown.clicked.connect(self.arrDownClicked)
        self.gridLayout.addWidget(self.arrDown, 2, 1, 1, 1)

        # self.hardReset()
        self.label_3.setText("HIGH SCORE")
        self.label_4.setText("SCORE")
        self.scoreHigh.setText("999999")
        self.scoreCurrent.setText("000009")
        self.arrRight.setText(">")
        self.arrUp.setText("^")
        self.arrLeft.setText("<")
        self.arrDown.setText("v")

    def newGame(self):
        self.timer.stop()

        # Poprawa wielkości rysowania przy zmianie długości boku
        self.cellWidth = int((self.width - 100) / self.cellCount)
        self.myCanvasSize = int(self.cellWidth * self.cellCount)
        self.myCanvasPaddingX = (self.width - self.myCanvasSize) / 2

        self.newDirection = ""
        self.Python.direction = ""
        self.Python.tail = []
        self.Python.head.x = int(self.cellCount/2)
        self.Python.head.y = int(self.cellCount/2)

        self.gameMatrix = []
        for i in range(self.cellCount):
            temp = []
            for j in range(self.cellCount):
                temp.append(0)
            self.gameMatrix.append(temp)

        if self.closedBox:
            for i in range(self.cellCount):
                self.gameMatrix[i][0] = 7
                self.gameMatrix[0][i] = 7
                self.gameMatrix[i][self.cellCount-1] = 7
                self.gameMatrix[self.cellCount-1][i] = 7

        if self.randomWall:
            randY1 = randrange(3, int(self.cellCount/2-2))
            randY2 = randrange(int(self.cellCount/2)+3, self.cellCount-3)
            for i in range(self.cellCount-6):
                self.gameMatrix[i+3][randY1] = 7
                self.gameMatrix[i+3][randY2] = 7

        self.gameOver = False
        self.timer.start(int(1000/self.CPS))
        # self.paintFlag = True
        # self.update()

    def onTimeout(self):
        self.paintFlag = True
        if not self.gameOver:
            self.gameStep()
        self.update()

    def gameStep(self):
        if self.checkCollision():
            self.gameOver = True
        else:
            self.moveSnake(self.checkFoodCollision())

    def checkCollision(self):
        if self.gameMatrix[self.Python.head.x][self.Python.head.y] == 7:
            return True
            # TODO dodać alert - wyskakujące okienko że game over

        for i in range(len(self.Python.tail)):
            if self.Python.tail[i].x == self.Python.head.x and self.Python.tail[i].y == self.Python.head.y:
                return True
                # TODO dodać alert - wyskakujące okienko że game over

        return False

    def checkFoodCollision(self):
        temp = self.gameMatrix[self.Python.head.x][self.Python.head.y]
        if temp == 1:
            # self.spawnFoodNormal() TODO
            # self.score+=1  TODO
            pass
        elif temp == 2:
            # self.spawnFoodSuper() TODO
            # self.score+=5 (balans później) TODO
            pass
        self.gameMatrix[self.Python.head.x][self.Python.head.y] = 0
        return temp

    def moveSnake(self, situation):

        # Zakaz pójścia węża 'w tył'
        tbool1 = self.newDirection == "N" and self.Python.direction == "S"
        tbool2 = self.newDirection == "E" and self.Python.direction == "W"
        tbool3 = self.newDirection == "W" and self.Python.direction == "E"
        tbool4 = self.newDirection == "S" and self.Python.direction == "N"
        if not (tbool1 or tbool2 or tbool3 or tbool4):
            self.Python.direction = self.newDirection

        if situation == 0:
            self.Python.tailMove()
            # self.Python.tailMoveEating() # do testów poruszania się, gdy nie ma jeszcze jedzenia na planszy
        elif situation == 1:
            self.Python.tailMoveEating()
        elif situation == 2:
            # TODO - przyspieszenie
            self.Python.tailMoveEating()

        if not self.closedBox:
            self.movementCorrection()

    def movementCorrection(self):
        if self.Python.head.x < 0:
            self.Python.head.x = self.cellCount-1
        elif self.Python.head.y < 0:
            self.Python.head.y = self.cellCount-1
        elif self.Python.head.x > self.cellCount-1:
            self.Python.head.x = 0
        elif self.Python.head.y > self.cellCount-1:
            self.Python.head.y = 0

    def paintEvent(self, e):
        if self.paintFlag:
            print("paint")

            # Kolory TODO self?
            backgroundColor = QColor(153, 204, 255)
            wallColor = QColor(0, 0, 0)
            foodNormalColor = QColor(255, 0, 0)
            foodSuperColor = QColor(255, 165, 0)
            snakeTailColor = QColor(0, 128, 0)
            snakeHeadColor = QColor(0, 100, 0)

            # Dla uproszczenia i skrócenia dalszej części
            width = self.myCanvasSize
            x0 = int(self.myCanvasPaddingX)
            y0 = int(self.myCanvasPaddingY)

            painter = QPainter(self)

            painter.setBrush(backgroundColor)
            painter.setPen(Qt.NoPen)  # rysowanie bez krawędzi
            painter.drawRect(x0, y0, width, width)  # tło

            for i in range(self.cellCount):
                for j in range(self.cellCount):

                    if self.gameMatrix[i][j] == 7:
                        painter.setBrush(wallColor)
                        # figura - kwadrat

                    elif self.gameMatrix[i][j] == 1:
                        painter.setBrush(foodNormalColor)
                        # figura - kółko? romb?

                    elif self.gameMatrix[i][j] == 2:
                        painter.setBrush(foodSuperColor)
                        # figura - kółko? romb?

                    else:
                        painter.setBrush(backgroundColor)

                    painter.drawRect(
                        int(x0+(i*self.cellWidth))
                        , int(y0+(j*self.cellWidth))
                        , int(self.cellWidth)
                        , int(self.cellWidth))

            # Rysowanie węża
            painter.setBrush(snakeTailColor)
            for i in range(len(self.Python.tail)):
                painter.drawRect(int(x0 + 1 + (self.Python.tail[i].x * self.cellWidth)),
                                 int(y0 + 1 + (self.Python.tail[i].y * self.cellWidth)),
                                 int(self.cellWidth)-2,
                                 int(self.cellWidth)-2)

            painter.setBrush(snakeHeadColor)
            painter.drawRect(int(x0+(self.Python.head.x * self.cellWidth)), int(y0+(self.Python.head.y * self.cellWidth)), int(self.cellWidth), int(self.cellWidth))

        self.paintFlag = False

    def arrRightClicked(self):
        self.newDirection = "E"

    def arrUpClicked(self):
        self.newDirection = "N"

    def arrLeftClicked(self):
        self.newDirection = "W"

    def arrDownClicked(self):
        self.newDirection = "S"

# TODO Usunąć
# app = QApplication(sys.argv)
# interface = GameView()
# interface.show()
# interface.newGame()
# sys.exit(app.exec_())
