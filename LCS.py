def main():
    file_input = input("Enter file name: ")

    with open(file_input, "r") as file:
        string = file.read()
        string = string.split("\n")

        table = make_table(string[0], string[1])
        print(LCS(table, string[0], string[1], len(string[0]), len(string[1])))
        print(LCS_all(table, string[0], string[1], len(string[0]), len(string[1])))

def make_table(string1, string2):
    table = [[0 for row in range(len(string2) + 1)] for col in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if (string1[i - 1] == string2[j - 1]):
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    return table

def LCS(table, string1, string2, i, j):
    if (i == 0 or j == 0):
        return ""

    if (string1[i - 1] == string2[j - 1]):
        return LCS(table, string1, string2, i - 1, j - 1) + string1[i - 1]

    if (table[i][j - 1] > table[i - 1][j]):
        return LCS(table, string1, string2, i, j - 1)

    return LCS(table, string1, string2, i - 1, j)

def LCS_all(table, string1, string2, i, j):
    if (i == 0 or j == 0):
        return [""]

    if (string1[i - 1] == string2[j - 1]):
        lcs = LCS_all(table, string1, string2, i - 1, j - 1)

        for Z in range(len(lcs)):
            lcs[Z] = lcs[Z] + string1[i - 1]

        return lcs

    R = []

    if (table[i][j - 1] >= table[i - 1][j]):
        R = LCS_all(table, string1, string2, i, j - 1)

    if (table[i - 1][j] >= table[i][j - 1]):
        R = R + LCS_all(table, string1, string2, i - 1, j)

    return R

def trim_edges(string1, string2):
    count = 0
    string1_end = len(string1)
    string2_end = len(string2)

    for i, j in string1, string2:
        if (i == j):
            count += 1
        else:
            break

    for i, j in reversed(string1), reversed(string2):
        if (i == j):
            string1_end -= 1
            string2_end -= 1

    return count, string1_end, string2_end

if __name__ == "__main__":
    main()