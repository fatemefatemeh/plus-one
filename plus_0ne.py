def plus_one(digits):
     digits = int("".join([str(x) for x in digits]))
     digits += 1
     return digits
    

print(plus_one(digits=[0,4,1,0]))

