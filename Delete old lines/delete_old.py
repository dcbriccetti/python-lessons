with open('data') as file:
    lines_read = 0
    while True:
        line = file.readline()
        lines_read += 1
        assert(line)
        if line.startswith('COPY "Table A"'):
            break
print('%d lines read' % lines_read)