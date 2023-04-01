from random import shuffle


def get_player_numbers():
    player_numbers = []
    for i in range(6):
        while True:
            try:
                number = int(input("Podaj liczbę od 1 do 49: "))
                if (1 <= number <= 49) and (number not in player_numbers):
                    player_numbers.append(number)
                    break
                else:
                    print("Wpisano nieprawidłowe dane. Podaj liczbę od 1 do 49."
                          "\nLiczby nie mogą się powtarzać: ")
            except ValueError:
                print("Wpisano nieprawidłowe dane. Podaj liczbę od 1 do 49: ")
    return player_numbers


player_numbers = get_player_numbers()
player_numbers.sort()
print("Twoje liczby: ", player_numbers)
LOTTO = [i+1 for i in range(0, 49)]
shuffle(LOTTO)
LOTTO_results = (LOTTO[:6])
LOTTO_results.sort()
print("Wylosowane liczby LOTTO", LOTTO_results)
happy_numbers = 0
for player_number in player_numbers:
    if player_number in LOTTO_results:
        happy_numbers += 1
print(f'Trafiłeś {happy_numbers} liczbę/y')
