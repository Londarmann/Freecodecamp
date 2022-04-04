def arithmetic_arranger(problems, val=False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    if len(problems) > 5:
        return "Error: Too many problems."
    for chars in problems:
        words = chars.split()
        length = 0
        for word in words:
            if len(word) > 4:
                return "Error: Numbers cannot be more than four digits."

            if word == "/" or word == "*":
                print(word)
                return "Error: Operator must be '+' or '-'."

            if not word.isdigit() and word != "+" and word != "-":
                return "Error: Numbers must only contain digits."

            if len(word) > length:
                length = len(word)
        length += 2

        for i in range(length - len(words[0])):
            line1 += ' '

        line1 += words[0]

        for i in range(4):
            line1 += ' '
        line2 += words[1]

        for i in range(length - len(words[2]) - 1):
            line2 += ' '

        line2 += words[2]

        for i in range(4):
            line2 += ' '

        for i in range(length):
            line3 += '-'

        for i in range(4):
            line3 += ' '

        sum_up = str(eval(chars))

        for i in range(length - len(sum_up)):
            line4 += ' '

        line4 += sum_up

        for i in range(4):
            line4 += ' '

    if val is True:
        return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}\n{line4.rstrip()}"
    return f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"
