print("1.---------------------------------")
# Знайди назву найдешевшого товару.
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600
}
res = min(products, key=products.get)
print(res)
#OR
res2 = [key for key,value in sorted(products.items(), key=lambda item:item[1])]
print(res2[0])

