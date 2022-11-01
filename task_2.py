strings=int(input("How many strings do you want to add ? : "))
string_list=[]
for item in range(strings):
    string_list.append(input("Whats your string? "))

max=-1
mex_string="hi"
for item in range(strings):
    print(len(string_list[item]))

    if len(string_list[item]) > max:
        max = len(string_list[item])
        mex_string=string_list[item]


# print(string_list[0])
print(mex_string)