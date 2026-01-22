# 1. Stwórz liste, która wypelnisz 10 liczbami całkowitymi
# i zwróć sumę wszystkich liczb z tej listy

numbers = [2,5,7,1,5,3,9,4,3,2]

print(f'Suma liczb w liście to: {sum(numbers)}')

#2. Stwórz liste, ktora bedzie zawierać 10słow.
#Nastepnie stworz druga liste, ktora bedzie
#zawierac tylko te slowa ktore maja wiecej niz 5 liter

words = ['hania', 'cos', 'tomasz', 'dom', 'talerz', 'krzeslo', 'okno', 'laptop', 'mysz', 'szklanka']

longer_words = []


for word in words:
    length = len(word)

    if length > 5:
        longer_words.append(word)

print(f'Słowa dłuższe niż 5 liter: {longer_words}')

# 3. Stwórz listę, którą wypełnisz 10 liczbami całkowitymi.
# Znajdz najmniejsza i najwieksza liczbe.

numbers2 = [6,1,6,8,9,3,5,2,0,7]
print(f'najmniejsza liczba to: {min(numbers2)}')
print(f'największa liczba to: {max(numbers2)}')

# 4. Stwórz listy, którą wypełnisz imionami - po 5 imion w każdej z list.
# Zadbaj o to, by niektóre imiona się powtarzały (czyli, żeby były obecne w obu listach).
# Wyswietl te imiona.

names1 = {'hania', 'tomek', 'marta', 'michal', 'lilka'}
names2 = {'mariusz', 'tomek', 'nadia', 'michal', 'marta'}

print(f'Wspólne imiona to: {names1 & names2}')

# 5. Korzystająć z list z poprzedniego ćwieczenia, wyswietl tylko te imiona,
# ktore są obecne w pierwszej liśćie.

print(f'Imiona tylko w pierwszej liscie to: {names1 - names2}')

# 6. Stwórz słownik, który będzie przechowywał informacje o krajach
# i ich stolicach. Dodaj do niego 5 elementów. Wyświetl dane ze słownika
# w formacie kraj - stolica czyli np. Polska - Warszawa

countries = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
    'Szwecja': 'Sztokcholm',
    'Ukraina': 'Kijow'
}

print('Kraje i stolice:')

for country, state in countries.items():
    print(country + ' - '+ state)

# 7. Posortuj słownik z poprzedniego ćwiczenia w kolejności alfabetycznej.

sorted_countries = sorted(countries.items())

print('Posortowane kraje i stolice:')

for country, state in sorted_countries:
    print(country + ' - '+ state)

# 8. Stwórz program, który prosi użytkownika o wpisanie tekstu w  konsoli,
# a następnie utwórz słownik, w którym kluczami będą słowa występujące
# w tym tekście, a wartościami liczby wystąpień każdego słowa. Wyświetl
#zawartość słownika.

text = input('Wprowadź tekst: ')
words = text.split()

counts_words = {}

for word in words:
    if word not in counts_words:
        counts_words[word] = 1
    else:
        counts_words[word] += 1

print('Wystąpienia słów w tekście: ')
for word, count in counts_words.items():
    print(word + ': ' + str(count))

# 9. Napisz program, w którym użytkownik wprowadzi imię, nazwisko, wiek,
# a następnie wyświetl te dane. Sprawdź, czy użytkownik jest pełnoletni
# oraz wyświetl odpowiednią informację.

name = input("Podaj swoje imię: ")
lastname = input("Podaj swoje nazwisko: ")
age = int(input("Podaj swój wiek: "))

print(f"Cześć {name} {lastname}, masz {age} lat.")

if age < 18:
    print("Jesteś osobą niepełnoletnią.")
else:
    print("Jesteś osobą pełnoletnią.")





