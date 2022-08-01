first = input()
second = input()
third = input()

def ohm(first, second, third):
    

    dic_color = {
        'black' : 0,
        'brown' : 1,
        'red' : 2,
        'orange' : 3,
        'yellow' : 4,
        'green' : 5,
        'blue' : 6,
        'violet' : 7,
        'grey' : 8,
        'white' : 9 
    }

    # list_mul = list(dic_color)
    # for i in range(len(list_mul)):
    #     list_mul[i] = 10 ** dic_color[list_mul[i]]             # 이게 더 비효율적인듯 (원래 딕셔너리 사용하려고함)

    dic_mul = {
        'black' : 1,
        'brown' : 10,
        'red' : 100,
        'orange' : 1000,
        'yellow' : 10000,
        'green' : 100000,
        'blue' : 1000000,
        'violet' : 10000000,
        'grey' : 100000000,
        'white' : 1000000000
    }


    first = dic_color[first] * 10
    second = dic_color[second]
    third = dic_mul[third]

    return (first + second) * third

print(ohm(first, second, third))