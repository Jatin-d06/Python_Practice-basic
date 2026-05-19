# # write a program to print  
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# a = "1"
# a *=1
# b = "2"
# b *=2
# c = "3"
# c *=3
# d = "4"
# d *=4
# e = "5"
# e *=5
# f = "6"
# f *=6

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

for i in range(1,7):
    print(f"{i}"*i)

i = 1
while i < 7:
    print(f"{i}*{i}")
    i = i+1