#1 Напишите программу, которая принимает на вход цифру,
#обозначающую день недели, и проверяет, является ли этот день выходным.


day = int(input('Введите число, обозначающее день недели '))
if (day >= 1) and (day <= 5):
    print('День недели под данным номером - рабочий день')
elif day == 6 or day == 7:
    print('День недели под данным номером - выходной день')
elif day > 7:
    print ("Акстись демон, ты от куда?")
