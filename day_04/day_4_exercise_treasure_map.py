# A caixa branca doi criada atravÃ©s de EMOJI link: https://getemoji.com/

# import sys
# import os

# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row3 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

position = str(input("Where do you want to put the treasure? "))
# ð¨ Don't change the code above ð

#Write your code below this row ð
x = int(position[0]) # horizontal
y = int(position[1]) # vertical

select_row = map[y - 1]
select_row[x - 1] = "X"

# map[y - 1][x - 1] = "X"


#Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"      ['1'] ['2'] ['3']\n['1'] {row1}\n['2'] {row2}\n['3'] {row3}")

# restart_program()