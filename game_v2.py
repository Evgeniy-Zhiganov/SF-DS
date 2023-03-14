"игра угадай число"
"Компьютер сам загадывает и угадывает число"

import numpy as np

def random_predict(number:int=1) -> int:
    """рандомно угадываем число
    Args: 
        number (int, optional): загаданное число. defoult to 1
        
    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) -> int:
    """ За какое в среднем количество попыток угадывается наше число

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"ваш алгоритм угадывает число в среднем за: {score} попыток")
    #return(score)
#RUN
if __name__ == '__main__':
    score_game(random_predict)
    

