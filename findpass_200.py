#       Qv49CmZB2Df4jB-
#       Qv49AmZB2Df4jB-
#       Py43CoZB,Lg4fB3
fkey = 'Tr43Fla92Ch4n93'
pic = open('src.jpg','rb').read()
print pic[:50]
key = ''

for i in range(len(fkey)):
	if i == 4:
		print ord(fkey[i])
		print pic[ord(fkey[i])]
		print ord(pic[ord(fkey[i])])
	v12 = ord(pic[ord(fkey[i])]) % 10
	if i % 2 == 1:
		key += chr(ord(fkey[i])+v12)
	else:
		key += chr(ord(fkey[i])-v12)

print key