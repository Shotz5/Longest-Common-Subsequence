def main():
    file_input = input("Enter file name: ")

    with open(file_input, "r") as file:
        string = file.read()
        string = string.split("\n")

        print(string)

        table = make_table(string[0], string[1])
        print(LCS(string[0], string[1], len(string[0]) - 1, len(string[1]) - 1, table))
        print(LCS_all(table, string[0], string[1], len(string[0]) - 1, len(string[1]) - 1))

def make_table(string1, string2):
    table = [[0 for col in range(len(string1) + 1)] for row in range(len(string2) + 1)]
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if (string1[i - 1] == string2[j - 1]):
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

    return table

# def LCS(table, string1, string2, i, j):
#     if (i == 0 or j == 0):
#         return ""

#     if (string1[i - 1] == string2[j - 1]):
#         return LCS(table, string1, string2, i-1, j-1) + string1[i - 1]

#     if (table[i][j-1] > table[i-1][j]):
#         return LCS(table, string1, string2, i, j-1)

#     return LCS(table, string1, string2, i-1, j)

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

def LCS(X, Y, m, n, lookup):
 
    # if the end of either sequence is reached
    if m == 0 or n == 0:
        # create a list with one empty string and return
        return ['']
 
    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
 
        # ignore the last characters of `X` and `Y` and find all LCS of substring
        # `X[0…m-2]`, `Y[0…n-2]` and store it in a list
        lcs = LCS(X, Y, m - 1, n - 1, lookup)
 
        # append current character `X[m-1]` or `Y[n-1]`
        # to all LCS of substring `X[0…m-2]` and `Y[0…n-2]`
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (X[m - 1])
 
        return lcs
 
    # we reach here when the last character of `X` and `Y` don't match
 
    # if a top cell of the current cell has more value than the left cell,
    # then ignore the current character of string `X` and find all LCS of
    # substring `X[0…m-2]`, `Y[0…n-1]`
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(X, Y, m - 1, n, lookup)
 
    # if a left cell of the current cell has more value than the top cell,
    # then ignore the current character of string `Y` and find all LCS of
    # substring `X[0…m-1]`, `Y[0…n-2]`
    if lookup[m][n - 1] > lookup[m - 1][n]:
        return LCS(X, Y, m, n - 1, lookup)
 
    # if the top cell has equal value to the left cell, then consider both characters
 
    top = LCS(X, Y, m - 1, n, lookup)
    left = LCS(X, Y, m, n - 1, lookup)
 
    # merge two lists and return
    return top + left


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