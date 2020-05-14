import random

def lenghtOfLongestAP(set):
    n = len(set)
    if (n <= 2):
        return n
    L = [[0 for x in range(n)]
         for y in range(n)]
    llap = 2
    for i in range(n):
        L[i][n - 1] = 2
    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while (i >= 0 and k <= n - 1):

            if (set[i] + set[k] < 2 * set[j]):
                k += 1

            elif (set[i] + set[k] > 2 * set[j]):
                L[i][j] = 2
                i -= 1

            else:
                L[i][j] = L[j][k] + 1
                llap = max(llap, L[i][j])
                i -= 1
                k += 1
                while (i >= 0):
                    L[i][j] = 2
                    i -= 1
    return llap


class pair_number_color:
    """
    Klasa na parę liczba, kolor.
    """
    def __init__(self, number, color=None):
        self.number = number
        self.color = color

def insert_number(list_, number):
    """
    Wstawia liczbę do listy par w kolejności rosnącej.
    :param list_: Lista par (liczba, krotka)
    :param number: Liczba którą wstawiamy
    :return: Lista par
    """
    if len(list_) == 0:
        list_.append(pair_number_color(number))
        return list_

    for i in range(len(list_)):
        if list_[i].number>number:
            list_.insert(i, pair_number_color(number))
            return list_
    list_.append(pair_number_color(number))
    return list_


# wstawia kolor do elementu który nie ma koloru
def insert_color(list_, color):
    """
    Wstawia kolor do listy par, wstawia go do pierwszego elementu który nie ma koloru
    :param list_: Lista par (liczba, krotka)
    :param color: Wstawiany kolor
    :return: Lista par
    """
    for p in list_:
        if p.color is None:
            p.color=color
            return

def find_longest_monochromatic_arithmetic(list_, max_number_color):
    """
    Zwraca najdłuższy monochromatyczny ciąg arytmetyczny w danym momencie
    :param list_: Lista par
    :param max_number_color: Liczba kolorów
    :return:
    """
    longest=0
    for c in range(1,max_number_color+1):
        one_color_list = [p.number for p in list_ if p.color == c]
        longest=max(lenghtOfLongestAP(one_color_list), longest)
    return longest

from math import gcd

def EKG_generator(size):
    """
    Generuje ciąg EKG o zadanej długości
    :param size: Liczba elementów tego ciągu
    :return: Lista elementów ciągu
    """
    #wiemy że ciąg EKG jest ograniozony z góry przez 14
    if(size==1): return [1]
    if(size==2): return [1, 2]
    if(size<1): raise ValueError("Nieprawidłowa długość")

    numberslist=list(range(3, 14*size))
    EKGlist = [1, 2]
    for i in range(size-2):
        index = 0
        while(gcd(EKGlist[-1], numberslist[index])==1):
            index=index+1
        EKGlist.append(numberslist.pop(index))
    return EKGlist

def method4(size):
    listnumberlist = [list(range(1, size+1))]
    sequence = []
    while len(listnumberlist) != 0:
        if len(listnumberlist[0]) == 0:
            listnumberlist.pop(0)
        else:
            middleindex=len(listnumberlist[0]) // 2
            sequence.append(listnumberlist[0][middleindex])
            if len(listnumberlist[0][:middleindex]) !=0:
                listnumberlist.append(listnumberlist[0][:middleindex])
            if len(listnumberlist[0][middleindex+1:]) != 0:
                listnumberlist.append(listnumberlist[0][middleindex+1:])
            listnumberlist.pop(0)
    return sequence

def print_numbers(list_):
    for n in list_:
        print(n, end="\t")

def print_colors(list_):
    for c in list_:
        if c is None:
            print("", end="\t")
        else:
            print(c, end="\t")

def input_range(maxlenght):
    try:
        l = int(input("Wpisz od której liczby losować: "))
        h = int(input("Wpisz do której liczby losować: "))
    except:
        print("Nie wpisano liczb")
        return input_range(maxlenght)

    if(h+1-l<maxlenght):
        print("Wybrano za mały przedział!")
        return input_range(maxlenght)
    computers_number = random.sample(range(l, h + 1), maxlenght)
    return computers_number

strategy_list = ["1. Losowy ciąg", "2. Kolejne liczy", "3. Ciąg EKG", "4. Połowy przedziałów"]

print("Witamy w grze Szmeredi Online.")
print("Wybierz parametry gry:")

while True:
    try:
        maxlenght = int(input("Długość monochromatycznego ciągu arytmetycznego: "))
        if(maxlenght>0):
            break
        else:
            print("Wpisałeś liczbę mnniejszą od 1")
    except:
        print("Nie podałeś liczby naturalnej!")

while True:
    try:
        number_of_colors = int(input("Liczba dostępnych kolorów: "))
        if (number_of_colors > 0):
            break
        else:
            print("Wpisałeś liczbę mnniejszą od 1")
    except:
        print("Nie podałeś liczby naturalnej!")

while True:
    try:
        size = int(input("Maksymalna długość rozgrywki: "))
        if (size > 0):
            break
        else:
            print("Wpisałeś liczbę mnniejszą od 1")
    except:
        print("Nie podałeś liczby naturalnej!")

while True:
    print("Wybierz strategię:")
    for s in strategy_list:
        print(s)
    print("q Opuść grę")
    strategy = input("Wciśnij q lub liczbę odpowiadającą wybranej strategii:")
    if strategy == "q":
        quit()
    try:
        strategy=int(strategy)
        computers_number = []
        if strategy == 1:
            computers_number = input_range(size)
            break
        if strategy == 2:
            computers_number = list(range(1, size + 1))
            break
        if strategy == 3:
            computers_number = EKG_generator(size)
            break
        if strategy == 4:
            computers_number = method4(size)
            break
        raise Exception
    except:
        print("Nie wybrałeś odpowiedniej strategii!")

list_ = []

for i in range(len(computers_number)):
    print("\n")
    print("Liczba wybrana przez komputera to "+ str(computers_number[i]))
    insert_number(list_, computers_number[i])
    print("Dotychczas wybrane liczby: ", end="")
    print_numbers([p.number for p in list_])
    print()
    print("Dotychczas wybrane kolorzy: ", end="")
    print_colors([p.color for p in list_])
    print()
    while True:
        try:
            c = int(input("Wybierz kolor: "))
            if 0<c<number_of_colors:
                break
            raise Exception
        except:
            print("Nie wybrano odpowiedniego koloru!")

    insert_color(list_, int(c))

    if find_longest_monochromatic_arithmetic(list_, number_of_colors) >= maxlenght:
        print("Wygrał gracz komputerowy")
        quit()
#    print("Najdłuższy monochromatycnzy podciąg arytmetyczno ma długość " + str(find_longest_monochromatic_arithmetic(list_, number_of_colors)))

print("Wygrał gracz")
quit()
