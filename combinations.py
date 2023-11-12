def Royal_Flash(arr_hand_cards):
    return 0

def Street_Flash(arr_hand_cards):
    return 0

def Kare(arr_hand_cards):
    for i, el in enumerate(list(arr_hand_cards.values())):
        if el==4:
            return 87+int(list(arr_hand_cards.keys())[i])
    return 0

def FullHouse(arr_hand_cards):
    counter=0
    elements=[]
    for i, el in enumerate(list(arr_hand_cards.values())):
        if el == 2 or el==3:
            elements.append(i)
            counter+=el
    if counter==5:
        keys_work = list(arr_hand_cards.keys())
        return 74+max(int(keys_work[elements[0]]), int(keys_work[elements[1]]))
    return 0

def Flash(arr_hand_cards):
    return 0

def Street(arr_hand_cards):
    print(arr_hand_cards)
    arr_hand_cards = sorted(arr_hand_cards.items())
    print(arr_hand_cards)
    counter = 0
    el=arr_hand_cards[0][0]
    for i in arr_hand_cards:
        if int(i[0]) == int(el)+1:
            counter += 1
        else:
            counter = 0
        el = i[0]
        if counter == 5:
            return 52 + int(el)
    return 0

def Triple(arr_hand_cards):
    counter = 0
    elements = [0, 0]
    for i, el in enumerate(list(arr_hand_cards.values())):
        if el == 3:
            elements.append(i)
            counter += el
    if counter != 0:
        keys_work = list(arr_hand_cards.keys())
        return 39 + max(int(keys_work[elements[0]]), int(keys_work[elements[1]]))
    return 0

def Two_pairs(arr_hand_cards):
    counter = 0
    elements = []
    for i, el in enumerate(list(arr_hand_cards.values())):
        if el == 2:
            elements.append(i)
            counter += el
    keys_work = list(arr_hand_cards.keys())
    if counter==6:
        keys_work.pop(keys_work.index(str(min(int(keys_work[elements[0]]), int(keys_work[elements[1]]), int(keys_work[elements[2]])))))
        print(keys_work)
        counter=4
    if counter == 4:
        return 26 + max(int(keys_work[elements[0]]), int(keys_work[elements[1]]))
    return 0

def Pair(arr_hand_cards):
    for i, el in enumerate(list(arr_hand_cards.values())):
        if el == 2:
            return 13 + int(list(arr_hand_cards.keys())[i])
    return 0

def High_Card(arr_hand_cards):
    return max(int(i) for i in list(arr_hand_cards.keys()))

def Combinations(arr_hand_cards):
    rank = 0
    functions_arr = [Royal_Flash, Street_Flash, Kare, FullHouse, Flash, Street, Triple, Two_pairs, Pair, High_Card]
    for i in functions_arr:
        rank+=i(arr_hand_cards)
        if rank!=0:
            return rank
    return rank
