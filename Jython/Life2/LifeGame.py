# Conway's Game of Life, for the Young Programmers Podcast

from javax.swing import JFrame, JPanel, JButton, JToggleButton, Timer
from java.awt import FlowLayout, GridLayout
from java.awt.BorderLayout import SOUTH
from GridMutator import GridMutator

class LifeGame(object):
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.timer = Timer(250, None, actionPerformed=self._step)
        self.gridMutator = GridMutator()

    def startGui(self):
        frame = JFrame("Life", defaultCloseOperation=JFrame.EXIT_ON_CLOSE)
        self.gridPanel = JPanel(GridLayout(self.numRows, self.numCols))
        self.cellButtons = self._doForAllCells(self._createCellButton)
        self.grid = self._doForAllCells(lambda r,c: False)
        frame.add(self.gridPanel)
        buttonPanel = JPanel(FlowLayout())
        stepButton = JButton("Step", actionPerformed=self._step)
        runButton = JToggleButton("Run", actionPerformed=self._run)
        buttonPanel.add(stepButton)
        buttonPanel.add(runButton)
        frame.add(buttonPanel, SOUTH)
        frame.pack()
        frame.locationRelativeTo = None
        frame.visible = True

    def _step(self, event):
        self.grid = self.gridMutator.generateNext(
            self._doForAllCells(lambda r,c: self.cellButtons[r][c].selected))
        self._doForAllCells(self._selectCellButtonFromGrid)

    def _run(self, event):
        if self.timer.running:
            self.timer.stop()
        else:
            self.timer.start()

    def _createCellButton(self, r, c):
        button = JToggleButton()
        s = button.preferredSize
        button.preferredSize = (s.height, s.height) # Make square
        self.gridPanel.add(button)
        return button

    def _doForAllCells(self, fn):
        return [[fn(r,c) for c in range(self.numCols)] for r in range(self.numRows)]

    def _selectCellButtonFromGrid(self, r, c):
        self.cellButtons[r][c].selected = self.grid[r][c]

LifeGame(15, 15).startGui()
