# Calcular IMC
# BMI = weight(kg) / (height)Â² (mÂ²)

# ð¨ Don't change the code below ð
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ð¨ Don't change the code above ð

#Write your code below this line ð

bmi = int(weight) / float(height) ** 2
print(int(bmi))