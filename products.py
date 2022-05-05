# while loop 不知道迴圈幾次
# for loop 清楚知道迴圈幾次

#讀取舊檔案+split 
#continue跳過本次迴圈，但還會持續下個迴圈(break為完全跳脫迴圈) 
product = [] #product為一節車廂
with open('file.csv','r',encoding='utf-8') as fff: #寫入及讀取皆須使用同編碼
	for line in fff:
		if 'product,price' in line:
			continue #跳出本次迴圈 #排除'product,price'讀進product清單裡
		name, price = line.strip().split(',') 
#strip可把\n消掉 split可把<,>視為分割，故把line分割成兩個字串並丟入name和price
		product.append([name,price])
print(product)

#使用者輸入名稱及價格(匯入資料)
while True:
	name  = input('請輸入商品名稱: ')
	if name == 'q':
		break 
	price = input('請輸入商品價格: ')
	p = [] #p車廂裡的座位
	p.append(name)
	p.append(price) #22 23 24行可簡寫成 p = [name , price]
	product.append(p) #更簡潔版:product.append([name , price])
print(product)

#印出商品價格
for p in product:
	print(p[0]) #p[0]為商品名稱 因先輸入name
	print(p[1]) #p[1]為商品價格 才再輸入price
	print(p[0],'的價格為',p[1])

#寫入新檔案
with open('file.txt','w') as f:
	for p in product:
		f.write('商品為'+ p[0] + '價格為' + p[1] + '\n') 
		#須注意+只能字串+字串 or 數字+數字，如果類型不同不能合併。

#encoding(編碼) csv需先設定成國際間常用的'utf-8'版本才能使中文字元不會變亂碼
with open('file.csv','w', encoding='utf-8') as ff: 
	ff.write('product,price\n') #製作 p[0] p[1] 的title
	for p in product:
		ff.write(p[0] +','+ p[1] +'\n') #需加','才能換列(__) 需加'\n'才能換行(|)
