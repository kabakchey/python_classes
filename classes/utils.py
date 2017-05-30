
def print_table(table):
    for row in table:
        for elem in row:
            print(elem, end="\t")
        print()


if __name__ == "__main__":

    table = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    print_table(table)

