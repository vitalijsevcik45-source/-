a = [2,15,50,13,4,7,9,30,43,21,'apple','melon', 'orange', 'kiwi', 'melon' 'pineapple', 'peach', 'pear', 'banana', 'grape']

int_list = []
str_list = []

for x in a:
  if isinstance(x, int):
    int_list.append(x)

for x in a:
  if isinstance(x, str):
    str_list.append(x)

int_list.sort()
str_list.sort()

main_sorted = int_list + str_list
even = [x for x in int_list if x % 2 == 0]
caps = [x.upper() for x in str_list]
print("Список а (числа):", int_list)
print("Cпиcок b (слова):", str_list)
print("Bідсортований список (int +str):", main_sorted)
print("Числа кратні 2:", even)
print("Слова капсом:", caps) 
