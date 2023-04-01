from random import shuffle


def get_player_numbers():
    player_numbers = []
    for i in range(6):
        while True:
            try:
                number = int(input("Podaj liczbę całkowitą od 1 do 49: "))
                if (1 <= number <= 49) and (number not in player_numbers):
                    player_numbers.append(number)
                    break
                else:
                    print("Wpisano nieprawidłowe dane. Podaj liczbę całkowitą od 1 do 49."
                          "\nLiczby nie mogą się powtarzać: ")
            except ValueError:
                print("Wpisano nieprawidłowe dane. Podaj liczbę całkowitą od 1 do 49: ")
    player_numbers.sort()
    return player_numbers


def get_lotto_numbers():
    lotto = [i + 1 for i in range(0, 49)]
    shuffle(lotto)
    lotto_results = (lotto[:6])
    lotto_results.sort()
    return lotto_results


player_numbers = get_player_numbers()
print("Twoje liczby: ", player_numbers)
LOTTO_results = get_lotto_numbers()
print("Wylosowane liczby LOTTO", LOTTO_results)
happy_numbers = 0
for player_number in player_numbers:
    if player_number in LOTTO_results:
        happy_numbers += 1
print(f'Trafiłeś {happy_numbers} liczb/ę/y')
