#new pascal code here

#3 
number = int(input("Type a number"))
final_list = []
num = [1]
for i in range(1,number+1):
    sublist = num * i
    final_list.append(sublist)
    print(final_list)
