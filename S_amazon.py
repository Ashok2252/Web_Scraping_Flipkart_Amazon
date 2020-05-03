from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.amazon.in/b/ref=s9_acss_bw_cg_compacc_1a1_w?node=15621166031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=Q8PGG45R6BHWB4T838X4&pf_rd_t=101&pf_rd_p=c07e3c5f-6d93-4bde-bc0b-6e1c58b04948&pf_rd_i=976392031"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class": "a-section acs-product-block acs-product-block--default"})
# print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])

price = container.findAll("div",{"class": "a-section a-spacing-micro acs-product-block__price"})
print(price[0].text)

# rating = container.findAll("div",{"class": "hGSR34"})
# print(rating[0].text)

filename = "products1.csv"
f = open(filename, "w")

headers = "Product_Name, Price \n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div",{"class": "a-section a-spacing-micro acs-product-block__price"})
    price = price_container[0].text.strip()

    # rating_container = container.findAll("div",{"class": "hGSR34"})
    # rating = rating_container[0].text

   #print("Product_Name:"+ product_name)
   #print("Price: " + price)
   #print("Ratings:" + rating)

    #String parsing
    trim_price=''.join(price.split(','))
    rm_rupee = trim_price.split('₹')
    add_rs_price = "Rs."+rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    # split_rating = rating.split(" ")
    # final_rating = split_rating[0]

    print(product_name.replace("," ,"|") +"," + final_price + "\n")
    f.write(product_name.replace("," ,"|") +"," + final_price + "\n")

f.close()