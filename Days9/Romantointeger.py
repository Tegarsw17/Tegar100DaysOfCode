def romtoint(rome):
    # print(type(rev))
    total = 0
    for i in range(len(rome)):
        rom_val = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(rome)):
            if i > 0 and rom_val[rome[i]] > rom_val[rome[i - 1]]:
                int_val += rom_val[rome[i]] - 2 * rom_val[rome[i - 1]]
            else:
                int_val += rom_val[rome[i]]
        return int_val

    #     print(rome[-(i + 1)])
    #     if rome[-(i + 1)] == "M":
    #         total += 1000
    #     elif rome[-(i + 1)] == "C" and rome[-i] == "M":
    #         total -= 100
    #     elif rome[-(i + 1)] == "D":
    #         total += 500
    #     elif rome[-(i + 1)] == "C" and rome[-i] == "D":
    #         total -= 100
    #     elif rome[-(i + 1)] == "C":
    #         total += 100
    #     elif rome[-(i + 1)] == "X" and rome[-i] == "C":
    #         total -= 10
    #     elif rome[-(i + 1)] == "L":
    #         total += 50
    #     elif rome[-(i + 1)] == "X" and rome[-i] == "L":
    #         total -= 10
    #     elif rome[-(i + 1)] == "X":
    #         total += 10
    #     elif rome[-(i + 1)] == "I" and rome[-i] == "X":
    #         total -= 1
    #     elif rome[-(i + 1)] == "V":
    #         total += 5
    #     elif rome[-(i + 1)] == "I" and rome[-i] == "V":
    #         total -= 1
    #     elif rome[-(i + 1)] == "I":
    #         total += 1
    #     print(total)
    # print(total)
    # print("--------------")


# romtoint("MCDXCVIII")
romtoint("XLII")
romtoint("LXII")
romtoint("IV")
