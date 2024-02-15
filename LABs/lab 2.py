def divisibleby3(list):
    return [x for x in list if x % 3 == 0]


def front_back(list1, list2):
    size_list1 = len(list1)
    size_list2 = len(list2)

    first_half_list1 = list1[:size_list1]
    second_half_list1 = list1[size_list1:]
    first_half_list2 = list2[:size_list2]
    second_half_list2 = list2[size_list2:]

    combined_list = first_half_list1 + first_half_list2 + second_half_list1 + second_half_list2

    print("Combined List:")
    print(combined_list)


def transpose(matrix):
    return [[x[i] for x in matrix] for i in range(len(matrix))]


def sort_tuple(list_tuple):
    return [(sorted(list_tuple, key=lambda x: x[1]))]


def multiple_tuple_elements(t2):
    return [tuple(t2[x] * t2[x+1] for x in range(0, len(t2)-1))]


def factor_count(l2):
    dict_factor = {}
    for i in range(1, max(l2)+1):
        a = 0
        for j in l2:
            if j % i == 0:
                a += 1

        dict_factor[i] = a

    return dict_factor


def stock_blocks():
    stock_blocks = []
    num_stocks = int(input("Enter the number of stocks: "))
    for i in range(num_stocks):
        purchase_date = input("Enter purchase date for stock {}: ")
        purchase_price = float(input("Enter purchase price for stock {}: "))
        shares = int(input("Enter number of shares for stock {}: "))
        symbol = input("Enter stock symbol for stock {}: ")
        current_price = float(input("Enter current price for stock {}: "))
        stock_blocks.append((purchase_date, purchase_price, shares, symbol, current_price))
    return stock_blocks


def gain_loss(stocks):
    total_gain_loss = 0
    for stock in stocks:
        shares = stock[2]
        purchase_price = stock[1]
        current_price = stock[4]

        gain_loss = shares * (current_price - purchase_price)
        total_gain_loss += gain_loss
    return total_gain_loss



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))

t1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print(sort_tuple(t1))

t2 = (1, 5, 7, 8, 10)
print(multiple_tuple_elements(t2))

l2 = [2, 4, 6, 8]
print(factor_count(l2))

stock_list = stock_blocks()
print(gain_loss(stock_list))