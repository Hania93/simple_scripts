# 1. Napisz program, który sprawdzi, czy podana przez użytkownika liczba jest parzysta, czy nieparzysta.
import random

number = int(input('Enter a number: '))

if(number % 2 == 0):
    print('Number is even')
else:
    print('Number is odd')


# 2. Napisz program, który sprawdzi, czy podana liczba jest > < = 0

numer = int(input('Enter a number: '))

if(numer > 0):
    print('Number is grather than 0')
elif(numer < 0):
    print('Number is less than 0')
else:
    print('Number is equal to 0')

# 3. Napisz program, który zapyta użytkownika o wynik na egzaminie (od 0 do 100) i wyswietli odpowiednia ocene.
# 90-100 ->5
# 80-89 -> 4
# 70-79 -> 3
# 60-69 -> 2
# ponizej 60 -> 1

exam_result = int(input('Enter your exam result: '))

if(exam_result > 90):
    print('Your grade from the exam is 5')
elif(exam_result > 80):
    print('Your grade from the exam is 4')
elif(exam_result > 70):
    print('Your grade from the exam is 3')
elif(exam_result > 60):
    print('Your grade from the exam is 2')
else:
    print('Your grade from the exam is 1')

# 4. Napisz program, który wyświetli liczby od 0 do 100

print('All integer numbers from 0 to 100')

for i in range(0, 101):
    print(i)

# 5. Napisz program, który wyświetli wszystkie liczby pierwsze od 1 do 100
print('All prime numbers from 0 to 100:')

for i in range(2, 101):
    is_prime = True
    n = int(i**1/2)
    for j in range(2, n+1):
        if ( i % j == 0 ):
            is_prime = False
            break
    if(is_prime):
        print(i)


# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych z przedziału 1-100

sum = 0
for i in range(1, 101):
    if(i % 2 == 0):
        sum += i

print(f'The sum is: {sum}')

# 7. Napisz program, który policzy pole prostokąta (uzytkownik podaje boki)
a = int(input('Enter a rectangle width: '))
b = int(input('Enter a rectangle height: '))

area = a*b

print(f'The area is: {area}')

# 8. Napisz program, który sprawdzi czy podane imię jest męskie czy żeńskie.

name = input('Enter your name: ')

if(name.endswith('a')):
    print('Your name is female')
else:
    print('Your name is male')


# 9. Pobierz od użytkownika 3 liczby całkowite i uporządkuj je w kolejności od najmniejszej do największej.

a = int(input('Enter a first number : '))
b = int(input('Enter a second number : '))
c = int(input('Enter a third number : '))

print(f' Sorted numbers:{sorted((a, b, c))}')



# 10. Stwórz grę, w której wylosujesz liczbę z przedziału 1-100, zapiszesz tą liczbę do zmiennej,
# a następnie poprosisz użytkownika o odgadniecie tej liczby. Po każdej próbie wyświetlaj informację, czy
# liczba podana przez użytkownika jest < > od wylosowanej. Gdy użytkownik odgadnie liczbę, zakończ grę.
# (znajdż info jak losować liczby całkowite w pythonie)
random_number = random.randint(1, 100)
print(f'random number is: {random_number}')

while(True):
    user_number = int(input('Enter a number: '))
    if(user_number == random_number):
        print(f'The number is equal to {user_number}')
        break

    elif(user_number > random_number):
        print(f'The number is grather than random number')

    elif (user_number < random_number):
        print(f'The number is less than random number')

