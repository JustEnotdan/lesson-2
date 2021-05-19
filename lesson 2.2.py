l = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(l)):
    b = 0
    if str(l[i]).find("+") != -1:
        b += 1
    l[i] = l[i].replace("+", "")
    if l[i].isdigit():
        a = str(l[i])
        if int(l[i]) < 10:
            a = "0" + a
        if b == 1:
            a = '+' + a
        a = '"' + a + '"'
        l[i] = a

c = ""

for i in range(len(l)):
    c += str(l[i]) + " "
print(c)
