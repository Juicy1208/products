# while loop 不知道迴圈幾次
# for loop 清楚知道迴圈幾次
product = []#product為一節車廂
while True:
	name  = input('請輸入商品名稱: ')
	if name == 'q':
		break 
	price = input('請輸入商品價格: ')
	p = [] #p車廂裡的座位
	p.append(name)
	p.append(price)
	product.append(p)
print(product)