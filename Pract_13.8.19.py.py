tic = int(input("Сколько билетов вы хотите приобрести? "))
vis=tic
mon=0
while vis!=0:
    age=int(input(f'Введите возраст гостя №{vis}'))
    if age<18:
        print('Вход бесплатный')
    elif 18<=age<25:
        print('Стоимость билета 990 р.')
        mon=mon+990
    else:
        print('Стоимость билета 1390 р.')
        mon=mon+1390
    vis-=1
if tic>3:
    mon=mon*0.9
    print('Ваша скидка 10%')
    print('Общая стоимость ваших билетов (руб):')
    print(mon)
else:
    print('Общая стоимость ваших билетов (руб):')
    print(mon)








