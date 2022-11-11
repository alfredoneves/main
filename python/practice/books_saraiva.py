import requests
from bs4 import BeautifulSoup

# format: https://www.saraiva.com.br/psicologia?_q=psicologia&map=ft
search = input("type the kind of book you want (exp: psicologia): ")
print("----------scraping----------\n")
r = requests.get(f"https://www.saraiva.com.br/{search}?_q={search}&map=ft")
soup = BeautifulSoup(r.text, "lxml")
boxes = soup.find_all("div", class_="vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4")	# find all boxes with the books information
for box in boxes:
	article = box.section.a.article	# article with all the information I need
	name = article.find('div', class_="vtex-product-summary-2-x-nameContainer flex items-start justify-center pv6").h3.span.text
	print(name)
	div2 = article.find('div', class_="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--container-price").div
	div3 = div2.find_all('div', class_="pr0 items-stretch flex")[1]
	try:
		span3 = div3.span.span.span
		prices = span3.find_all('span')	# takes the price values like R$ 10,00
		for price in prices:
			print(f"{price.text}",end='')
		print("")
		print("--------------------------------------------------")
	except:
		print("book unavailable")
		print("--------------------------------------------------")
print(f"{len(boxes)} books found")

