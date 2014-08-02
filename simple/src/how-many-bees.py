from math import ceil

BEES_PER_ROW = 5 # This is all caps because it is a constant
manyBeeNums = (4, 5, 6, 9, 10, 11, 20, 21) # For testing, run repeatedly with these numbers of bees

for beeNums in manyBeeNums:
    numRows = ceil(beeNums / BEES_PER_ROW) # Rounds up if not evenly divisible
    remainderBees = beeNums % BEES_PER_ROW
    numBeesLastRow = remainderBees if remainderBees else BEES_PER_ROW

    print("\nBees: %d, rows: %d, bees in last row: %d" % (beeNums, numRows, numBeesLastRow))

    for row in range(numRows):
        numBeesThisRow = numBeesLastRow if row == numRows - 1 else BEES_PER_ROW
        for column in range(numBeesThisRow):
            print("Bee at row %d, column %d" % (row, column))
