numbers = [0, 20, 100, 1000, 500, 700]
fi = numbers[0]
se = numbers[0]
for i in numbers:
    if i > fi:
       se = fi
       fi = i
    if se < i and i < fi:
        se = i 
print(se)   