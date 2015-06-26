class CommandLine:
    def set(self, line):
        self.line = line
        spaceIndex = line.find(' ')
        if spaceIndex > 0:
            self.cmd = line[0:spaceIndex]
            self.args = line[spaceIndex + 1:]
        else:
            self.cmd = line
            self.args = ""

