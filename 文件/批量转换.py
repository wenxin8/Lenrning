import os
path = input('请输入路径')
for root,dirs,files in os.walk(path):
	# for dir in dirs:
	# 	print(os.path.join(root,dir))

	for file in files:
		# print(os.path.join(root,file))
		if file.endswith('.ipynb'):
			os.system('jupyter nbconvert --to html' + os.path.join(root,file))