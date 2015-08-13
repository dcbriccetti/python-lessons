with open('in.txt') as in_file:
    with open('out.txt', 'w') as out_file:
        for line in in_file:
            words = line.strip().split(' ')
            for word in words:
                if 'e' not in word:
                    out_file.write(word + ' ')
