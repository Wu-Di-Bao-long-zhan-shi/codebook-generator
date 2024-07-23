count = 0


def combination(num, *args):
    global count
    if num > 0:
        num -= 1
        for ii in chars:
            combination(num, *args, ii)
    else:
        count += 1
        w_j.write("".join(args) + "，")
        if count == 20:
            w_j.write("\n")
            count = 0


lowercase_characters = []
uppercase_characters = []
digit = []
special_characters = []

for i in range(32, 127):
    i_chr = chr(i)
    if i_chr not in lowercase_characters and i_chr not in uppercase_characters and i_chr not in digit:
        special_characters.append(i_chr)
for i in range(10):
    digit.append(str(i))
for i in range(65, 91):
    uppercase_characters.append(chr(i))
for i in range(97, 123):
    lowercase_characters.append(chr(i))


while True:
    try:
        character_selection = input("输入你选择的字符范围，1.小写字母 2.大写字母 3.数字 4.特殊符合\n" + \
                                    "(你输入的形式为 数字+数字, 例：1+2 或 2+3 或 1 或 2+3+4)\n").split("+")
        chars = []
        for i in character_selection:
            if i == "1":
                chars += lowercase_characters
            if i == "2":
                chars += uppercase_characters
            if i == "3":
                chars += digit
            if i == "4":
                chars += special_characters
        if not chars:
            raise FileNotFoundError

        number_digits = input("输入输出的密码为数, 几到几\n" + \
                              "如1-2, 3-3\n").split("-")
        path = input("密码本地址：")

        print("创建中")

        with open(f"{path}\密码本.txt", "w", encoding="utf-8") as w_j:
            for i in range(int(number_digits[0]), int(number_digits[1]) + 1):
                combination(i)

        if input("是否继续(回答是/否)") == "否":
            break
    except FileNotFoundError:
        print("出现错误, 请检查是否输入正确")


