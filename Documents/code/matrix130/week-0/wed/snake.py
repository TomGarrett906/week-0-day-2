# x = 5
# print(min(6,9))
# some_list = [6, 7 , 8, 43]
# def func(name):
#     print(name)

# whatever_num % 2 == 0:  GOOD FOR ODD OR EVEN!!!

# sum1 = 4+5
# sub1 = 5-4
# prod = 4*5
# div1 = 25/5
# floor_div = 7//3
# rem = 7%3
# exp = 5**2
# print(sum1, sub1, prod, div1, floor_div, rem, exp)
# print(int(div1))
# print(int(5.9))

str1 = "this is a string" #this is a comment
str2 = "so\'s this"
# print(str1, '\t', str2)

# str3 = str1 + ' ' + str2
# print(str3)
# first_name = 'Tom'
# fname = "Toby"
# print(f"Hello there {fname}!")

# a_list = ['abc', 4, True, [], 987]
# print(a_list)
# num_list = [23, 456, 56, 78, 1, 1897]
# print(sum(num_list))
# print(min(num_list))
# print(max(num_list))
# print(num_list[-1])
# print("another list:--> \n\n ")
# print(len(num_list))

# list.append()
# .pop()
# .remove()
# .insert()

# l_list = [23, 456, 56, 78, 1, 1897]

# for l in l_list:
#     print(l)
# for x in range(5):
#     print(x)

# for i in range(len(l_st)):
#     print(i)

# l_st = 'TOM'
# l = 0
# while l < len(l_st):
#     if l_st[1] == 'F':
#         print('FOUND IT!') 
#     elif l_st[1] == 'T':
#         print('Its here')
#     else:
#         print("not here")
#     print(l_st[1])
#     l = l + 1
print("Func test:")
def age_filter(user_age):
    # user_age = int(input("youre age: "))
    if user_age < 18:
        print('Minor')
    elif user_age >= 18 and user_age <= 65:
        print('Adult')
    else:
        return('Senior')
print(age_filter(98))

def multiply(a, b):
    return a * b






