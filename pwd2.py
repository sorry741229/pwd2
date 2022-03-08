ans = 'a123456'
x = 3 #初始機會
while True :
	pwd = input('請輸入密碼: ')
	if pwd == ans:
		print('登入成功')
		break
	else:
		x = x -1
		if x == 0:
			print('已輸入超過三次，結束')
			break
		print('密碼錯誤! 還有', x,'次機會')
		