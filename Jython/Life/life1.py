# Conway's Game of Life, for the Young Programmers Podcast

from javax.swing import JFrame, JPanel, JButton, JToggleButton, JCheckBox, Timer
from java.awt import FlowLayout, GridLayout
from java.awt.BorderLayout import SOUTH
from GridMutator import GridMutator

class LifeGame(object):
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.timer = Timer(250, None, actionPerformed=self._step)

    def startGui(self):
        frame = JFrame("Life", defaultCloseOperation=JFrame.EXIT_ON_CLOSE)
        (R, C) = (self.numRows, self.numCols)
        gridPanel = JPanel(GridLayout(R, C))
        self.checkBoxes = [[JCheckBox() for c in range(C)] for r in range(R)]
        self.grid = [[False for c in range(C)] for r in range(R)]
        for r in range(R):
            for c in range(C):
                gridPanel.add(self.checkBoxes[r][c])
        frame.add(gridPanel)
        buttonPanel = JPanel(FlowLayout())
        stepButton = JButton("Step", actionPerformed=self._step)
        runButton = JToggleButton("Run", actionPerformed=self._run)
        buttonPanel.add(stepButton)
        buttonPanel.add(runButton)
        frame.add(buttonPanel, SOUTH)
        frame.pack()
        frame.locationRelativeTo = None
        frame.visible = True

    def _getGridFromCheckBoxes(self):
        return [[self.checkBoxes[r][c].selected for c in range(self.numCols)]
            for r in range(self.numRows)]

    def _step(self, event):
        self.grid = GridMutator().generateNext(self._getGridFromCheckBoxes())
        self._selectCheckBoxesFromGrid()

    def _run(self, event):
        if self.timer.running:
            self.timer.stop()
        else:
            self.timer.start()

    def _selectCheckBoxesFromGrid(self):
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.checkBoxes[r][c].selected = self.grid[r][c]

LifeGame(15,15).startGui()