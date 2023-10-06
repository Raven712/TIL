word = "HappyHacking"

count = 0
mo = ['a', 'e', 'i', 'o', 'u']
for char in word:
    if char in mo:
        count += 1

print(count)
#까먹었는데 하여튼 저렇게 할거면 if char == 'e' 이런식으로 늘려가야하는걸로 암..