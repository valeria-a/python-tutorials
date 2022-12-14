#
# E    H
# B  S I  G
# A I  R N
# Y    I
#
# E         N
# B       I G
# A     R
# Y   I
# I H
# S

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    str_len = len(s)
    new_str = ""

    diff = 2 * numRows - 2

    for i in range(numRows):

        for j in range(i, str_len, diff):
            new_str += s[j]

            if (0 < i < numRows - 1) and j + diff - (2 * i ) < str_len:
                new_str += s[j + diff - (2 * i)]

    return new_str

print(convert('EBAYISHIRING', 6))

