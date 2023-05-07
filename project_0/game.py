"игра угадай число"

import numpy as np

number = np.random.randint(1,101)

count = 0

while True:
    count+=1
    predict_number = int(input("угадай число от 1 до 100: "))
    
    if predict_number < number:
        print("число должно быть больше")
        
    elif predict_number > number:
        print("число должно быть меньше")
    
    else:
        print(f"Поздавляем! Вы угадали число, это {number}, затрачено попыток {count}.")
        break