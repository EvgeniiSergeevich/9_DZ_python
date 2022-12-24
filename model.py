import random

candies = 117
i = 1




def candy_word(take):
    lcw = ['конфету', "конфеты", "конфет"]          # Вывод сообщения с правильным окончанием
    
    if take % 100 in range(10, 21):
        candy_word = lcw[2]
    elif take % 10 == 1:
        candy_word = lcw[0]    
    elif take % 10 in range(2, 5):
        candy_word = lcw[1]
    else:
        candy_word = lcw[2]
    return candy_word

def user_logic(take):
    global i, candies

    while candies > 0:
        try:
            take = int(take)
        except:
            return  "Вы ввели не число!"
            
        if take < 0 or take > 28:
            return  f"Нельзя забрать {take} {candy_word(take)}!"
            
        elif candies < take:
            return  f"Нельзя забрать {take} {candy_word(take)}. Остаток: {candies} шт!"
           
        elif take > 0 and take < 29:
            candies -= take
            i += 1
            return  f"ВЫ забрали {take} {candy_word(take)}."
   



def bot_logic():
    global candies, i
    if candies < 29:
        take = candies
        candies -= take
        i += 1
        return f'Бот забрал {take} {candy_word(take)}!'
    elif candies > 29 and candies < 58:
        c = [k for k in range(30, 58)]
        for j in range(len(c)):
            if candies == c[j]:
                take = j + 1
        candies -= take
        i += 1
        return f'Бот забрал {take} {candy_word(take)}!'
    elif candies > 58 and candies < 87:
        c = [k for k in range(59, 87)]
        for j in range(len(c)):
            if candies == c[j]:
                take = j + 1
        candies -= take
        i += 1         
        return f'Бот забрал {take} {candy_word(take)}!'
    else:
        take = random.randint(1, 28)
        candies -= take
        i += 1  
        return f'Бот забрал {take} {candy_word(take)}!'



def won():
    if candies == 0:
        if i % 2 == 0:                                          
            return 'Вы победили!!! УРА!'            
        else:
            return 'Бот победил!!! Не расстраивайся!'
        
    else:
        return f'Осталось {candies} {candy_word(candies)}'
           