#문서길이 최대 2500 단어길이는 최대50

doc = list(input())
word = input()

list_ = [] # doc의 앞글자부터 하나씩 넣을곳?
count = 0
for i in range(len(doc)):
    list_.append(doc[i])        #list_에 doc 앞글자를 다 집어넣음.
    word_ = ''.join(list_)  #그걸 하나의 단어로 만듬
    if word in word_:           #그게 찾고자하는 단어와 같을때 라고 처음에 했으나 (if word_ == word) 그렇게하면 abababa 에서 aba를 찾을떄, 처음 aba찾고나면 baba가 등록되는데 baba에 aba가 있어도 찾질못함.
        count += 1                  #그래서 위처럼 찾고자 하는 단어가 join으로 연결된 단어에 있을때.. ㅇㅇ
        list_ = []  

print(count)



# ababa
# word_ 

#aba -> word_ 
# abababa 
# aba -> 
# baba  ... 