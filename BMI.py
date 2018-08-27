user_height = input('Enter User\'s Height(cm):')
user_weight = input('Enter User\'s Weight(kg):')
user_height = float(int(user_height) / 100) 
user_weight = float(user_weight)

BMI = user_weight / ((user_height) * (user_height))
BMI = float(BMI)

print(BMI)

if BMI < 18.5:
	print('過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >=30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
