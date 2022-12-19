#return

def cube (num):
    return num*num*num

result = cube(4)
print (result)


#if command

is_male = False
is_tall = True

if is_male and is_tall:
    print('You are male and you are tall')
elif is_male and not(is_tall):
    print ('You are male and you are not tall')
elif not(is_male) and is_tall:
    print('You are not male and you are tall')
else:
    print ('You are neither male or tall')

 