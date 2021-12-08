# pointers
# split function
# list.append
# try catch inside for loop
# function with class file example parse
# type(str)
# abs value

# Split function
# str = "a-b-c-d-e-fg-h-i-jk,qwe"
# parse_str = str.split(',')
# print (str)
# print (parse_str[0].split(','))
# print (parse_str[1])
# print (parse_str)



# # List 
# init_list = [1,2,3,4]
# init_list.append(5)
# init_list.append(6)
# init_list.append(7)
# init_list.append([8,9,0,1])
# print (init_list)
# print (init_list[7][0])


# Try-except
# try:
#     val1 = int(input("Enter a number:"))
#     print (val1)
# except Exception as error:
#     print ("ERROR MESSAGE:", error)

items = [1,2,3,4,"Dog",5,6,7,8]
for item in items:
    try:
        print (int(item))
    except Exception as e:
        print(e)
        pass

# items = [1,2,3,4,"Dog",5,6,7,8]
# for item in items:
#     # print (str(type(item)))
#     if str(type(item)) == "<class 'int'>":
#         print (item)

# class Operator:

#     def add():
#         print ("Add")

#     def sub():
#         print ("Sub")

# def parse(input):
#     return input.split(',')

# if __name__ == '__main__':
#     op = Operator
#     op.add()

    # str_comb = "1m,12,1,1,1,1,2,3,4,5123,"
    # parsed_str = parse(str_comb)
    # print (parsed_str)


# Absolute value
# val1 = -10
# print (abs(val1))

# Enter values that you want to multiply?
# 1,3,64,0,8,89,13....