print("1.-----------------------------------------------------------------")
#Знайди найдорожчий товар, ціна якого менша за 700.
products = {
    "laptop": 1200,
    "phone": 800,
    "mouse": 25,
    "keyboard": 70,
    "monitor": 300,
    "tablet": 600,
    "webcam": 50
}
cheaper = {key:value for key,value in products.items() if value < 700}
print(cheaper)
max_val = max(cheaper.values())
res = [key for key,value in cheaper.items() if value == max_val]
print(res[0])