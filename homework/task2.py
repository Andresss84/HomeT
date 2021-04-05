#1
def is_palindrom(s):
    return s == s[: : -1]
is_palindrom('yey')
print(is_palindrom('yey'))

#2
s = 'hollywood'
s.count('o')
print(s.count('o'))

#3
a =['Oman', 'Belarus', 'Chile', 'Cuba', 'Egypt', 'Sweden', 'Peru', 'Kenya', 'Bahrain', 'Russia'];
answer = []
for i in a:
    if len(i) > 5:
        answer.append(i)
        print(answer.append(i))
    if 'A' in i:
        i.replace('A', 'a')
        print(i.replace('A', 'a'))

#4
d = 'Real Madrid is the best club'
d = ''.join(d.split())
print(''.join(d.split()))

#5
s = input('djhfhskslwwov')
s_new = ''
for i in range(len(s)):
 if s_new.find(s[i]) == -1 and s[i] != '':
        s_new += s[i]
print(s_new)
#6
f = input('Real Madrid is the best club')
len(f.split())
print(len(f.split()))
#7

