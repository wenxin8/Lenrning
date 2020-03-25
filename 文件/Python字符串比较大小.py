#字符串按位比较，两个字符串第一位字符的ascii码谁大，
#字符串就大，不再比较后面的；第一个字符相同就比第二个字符串，
#以此类推，需要注意的是空格的ascii码是32，空（null）的ascii码是0，
#大写字母和小写字母的ASCII不同
m = ["abc","Abc","bac","abc"]
print(m[0] == m[1])
print(m[0] == m[2])
print(m[0] == m[3])

#ord()和chr()分别表示将字符转换成ASCII和将ASCII转换成字符
m = ["a", "b", "A"]
print(ord(m[0]), ord(m[1]), ord(m[2]))
m = [97, 98, 65]
print(chr(m[0]), chr(m[1]), chr(m[2]))
