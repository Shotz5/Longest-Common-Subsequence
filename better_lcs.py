# LCS with DP (Optimal Space Complexity)

print("String 1: ")
string_1 = str(input())
print("String 2: ")
string_2 = str(input())
print("String 1: " + string_1 + " ... Length of String 1: " + str(len(string_1)))
print("String 2: " + string_2 + " ... Length of String 2: " + str(len(string_2)))

len_1 = len(string_1)
len_2 = len(string_2)

def uno_reverse(string_1, string_2, len_1, len_2):
    return string_2, string_1, len_2, len_1

if len_2 > len_1:
    string_1, string_2, len_1, len_2 = uno_reverse(string_1, string_2, len_1, len_2)

table = [[0] * (len_1 + 1) for row in range(2)]

def lcs(string_1, string_2):
    lcs = ""
    prev_max_eval = 0
    for row in range(len_1):
        bin_row = row % 2
        for col in range(len_2):
            if string_1[row] == string_2[col]:
                table[bin_row][col + 1] = table[1 - bin_row][col] + 1
            else:
                table[bin_row][col + 1] = max(table[1 - bin_row][col + 1], table[bin_row][col])
            if table[bin_row][col + 1] > prev_max_eval:
                prev_max_eval = table[bin_row][col + 1]
                lcs = lcs + string_2[col] # You could also do string_2[col] to appear less sus
    return table[bin_row][len_2], lcs

print(lcs(string_1, string_2))

for row in table:
    print(row)