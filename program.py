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
    def __init__(self, number, color=None):
        self.number = number
        self.color = color


#wstawia liczbę bez koloru
def insert_number(list_, number):
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
    for p in list_:
        if p.color is None:
            p.color=color
            return

def find_longest_monochromatic_arithmetic(list_, max_number_color):
    longest=0
    for c in range(max_number_color):
        one_color_list = [p.number for p in list_ if p.color == c]
        longest=max(lenghtOfLongestAP(one_color_list), longest)
    return longest

#losuje liczby z zakresu
computers_number = random.sample(range(0, 1000), 10)
number_of_colors=4
list_ = []

for i in range(len(computers_number)):
    print("\n")
    print("Liczba wybrana przez komputera to "+ str(computers_number[i]))
    insert_number(list_, computers_number[i])
    print("Dotychczas wybrane liczby: ", end="")
    print([p.number for p in list_])
    print("Dotychczas wybrane kolorzy: ", end="")
    print([p.color for p in list_])
    print()
    c = input("Wybierz kolor ")
    insert_color(list_, int(c))
    print("Najdłuższy monochromatycnzy podciąg arytmetyczno ma długość " + str(find_longest_monochromatic_arithmetic(list_, number_of_colors)))

