from random import shuffle
number1 = int(input("Podaj liczbę od 1 do 49: "))
number2 = int(input("Podaj liczbę od 1 do 49: "))
number3 = int(input("Podaj liczbę od 1 do 49: "))
number4 = int(input("Podaj liczbę od 1 do 49: "))
number5 = int(input("Podaj liczbę od 1 do 49: "))
number6 = int(input("Podaj liczbę od 1 do 49: "))
player_numbers = [number1, number2, number3, number4, number5, number6]
player_numbers.sort()
print(player_numbers)
LOTTO = [i+1 for i in range(0, 49)]
shuffle(LOTTO)
LOTTO_results = (LOTTO[:6])
LOTTO_results.sort()
print(LOTTO_results)
happy_numbers = 0
for player_number in player_numbers:
    if player_number in LOTTO_results:
        happy_numbers += 1
print(happy_numbers)
