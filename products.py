#建立記帳程式(二維清單)

#讓使用者重複商品名稱，就他購買過的東西
#因為「重複」,且不知道購買次數不一定,用while loop 會比較適合

products = [] #products商品 #4.設定清單為products(等等裡面就會裝一推商品)
while True:
	name = input('請輸入商品名稱:') #1.name名稱為變數,讓使用者輸入名稱
	if name == 'q': #2.name是q(quit)的話
		break#3.離開迴圈
	price = input('請輸入商品價格:') #6.price 價格 #price名稱為變數,讓使用者輸入價格
	p = [] #7.建立小清單，小清單變數設成P
	p.append(name)#8.把name裝進加入p小清單
	p.append(price)#9.把price裝進加入p小清單
	products.append(p)#10.把p裝進加入products大清單
	#products.append(name) #5.把name裝進加入products清單
print(products)#11

for product in products: #12.把products的清單一個一個拿出來，這一個一個為product
	print(product)#13.把小清單一個一個取出來
	print(product[0],'的價格是', product[1])#14.小清單第0個位置為名稱 第1個位置為價格


products[0][0] #外面0為products的第0大格，裡面的0為小清單的第0小格 (白話:把第0格的商品拿出來) #電腦都是從0開始算

#縮寫:

#products = [] 
#while True:
	#name = input('請輸入商品名稱:') 
	#if name == 'q':
		#break
	#price = input('請輸入商品價格:')
	#products.append([namr , price]) #直接簡寫 小清單直接裝入大清單
#print(products)

#解答:
#[['珍珠奶茶', '60'], ['紅茶', '25']]
#['珍珠奶茶', '60']
#珍珠奶茶 的價格 60
#['紅茶', '25']
#紅茶 的價格是 25