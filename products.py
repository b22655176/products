#建立記帳程式(二維清單)

#讓使用者重複商品名稱，就他購買過的東西
#因為「重複」,且不知道購買次數不一定,用while loop 會比較適合
#字串可以做 + 跟 * EX:'abc'+'123'='abc123'  /  'abc * '3' ='abcabcabc'
#+法 只能字串對字串,整數對整數 ,所以要把整數便字串,前面要加 string(字串的全名)(縮寫str) - str()
#創造出檔案(txt Or csv)
products = [] #products商品 #4.設定清單為products(等等裡面就會裝一推商品)
while True:
	name = input('請輸入商品名稱:') #1.name名稱為變數,讓使用者輸入名稱
	if name == 'q': #2.name是q(quit)的話
		break#3.離開迴圈
	price = input('請輸入商品價格:') #6.price 價格 #price名稱為變數,讓使用者輸入價格
	price = int(price) #把字串變成整數 因為價錢是整數
	p = [] #7.建立小清單，小清單變數設成P
	p.append(name)#8.把name裝進加入p小清單
	p.append(price)#9.把price裝進加入p小清單
	products.append(p)#10.把p裝進加入products大清單
	#products.append(name) #5.把name裝進加入products清單
print(products)#11

for product in products: #12.把products的清單一個一個拿出來，這一個一個為product
	print(product)#13.把小清單一個一個取出來
	print(product[0],'的價格是', product[1])#14.小清單第0個位置為名稱 第1個位置為價格
 
#創造寫入的檔案 (先打開檔案->用for loop把商品一個一個寫進去 #有寫到f.write才是真正的寫入)
with open ('products.csv', 'w', encoding='utf-8') as f:  #15.打開這個檔案，把檔案當作f #檔案.txt(筆記本) #檔案.csv(可用excel(用,可以跳格))
 	f.write('商品,價格\n')# 18.在f檔案 寫入商品與名稱(用,來跳格)(用\n來分行)
 	for p in products:#16.把檔案中的每一行的小清單一個一個拿出來
 		f.write(p[0] + ',' + str(p[1]) + '\n') #17.用+法把4個字串，變成一個字串，把大字串丟入write的功能，在這個f檔案 #\n換行 #檔案.csv(可用excel(用,可以跳格)) 





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