first_name = "Софія"
last_name = "Мартинюк"
age = 16

if type(first_name) == type(last_name) and first_name != last_name:
    print("Тип данних імені: ", type(first_name))
elif type(first_name) != type(last_name):
    print("Типи данних не співпадають.")
else:
    print(first_name, last_name)

if type(age) == int:
    print("Тип данних віку int ")
else:
    print("Тип данних віку не int")

list = [first_name, last_name]
print(list)