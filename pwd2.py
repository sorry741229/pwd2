ans = 'a123456'
x = 3 #初始機會
while x > 0 :
	pwd = input('請輸入密碼: ')
	if pwd == ans:
		print('登入成功')
		break
	else:
		x = x -1
		print('密碼錯誤! 還有', x,'次機會')
print('已輸入超過三次，結束')
		