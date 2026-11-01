print("1.--------------------------------------------------------------------")
# Найпопулярніша категорія товарів
#
#1.Порахуй кількість товарів у кожній категорії.
#2.Знайди категорію з найбільшою кількістю товарів.
#3.Якщо кілька категорій мають однакову кількість, вибери категорію за алфавітом.
#4.Виведи назву категорії та всі товари цієї категорії за алфавітом.
products = {
    "laptop": {"category": "electronics", "price": 1200},
    "phone": {"category": "electronics", "price": 800},
    "chair": {"category": "furniture", "price": 150},
    "table": {"category": "furniture", "price": 300},
    "mouse": {"category": "electronics", "price": 25},
    "desk": {"category": "furniture", "price": 250},
    "book": {"category": "education", "price": 30},
    "course": {"category": "education", "price": 100}
}
category_count = {}
for key, value in products.items():
    cat = value["category"]
    category_count[cat] = category_count.get(cat, 0)+1
print(category_count)
srt = sorted(category_count.keys(), key=lambda item:(
    -category_count[item],
    item
))
most_popul_cat = srt[0]
print(most_popul_cat)
prod = [product[0] for product in products.items() if product[1]["category"] == most_popul_cat]
print(prod)

print("2.-------------------------------------------------------------------")
# Найкращий товар у категорії
#Знайди найкращий товар серед категорії electronics.
#Критерії:
#1. Найвищий рейтинг.
#2. Якщо рейтинг однаковий — найнижча ціна.
#3. Якщо ціна також однакова — назва за алфавітом.
#Виведи назву товару та його рейтинг.
products = {
    "laptop": {"category": "electronics", "price": 1200, "rating": 4.8},
    "phone": {"category": "electronics", "price": 800, "rating": 4.8},
    "mouse": {"category": "electronics", "price": 25, "rating": 4.5},
    "keyboard": {"category": "electronics", "price": 70, "rating": 4.8},
    "chair": {"category": "furniture", "price": 150, "rating": 4.6}
}
elec = {}
for key,value in products.items():
    if value["category"] == "electronics":
        elec[key] = value
print(elec)
srt = sorted(elec.keys(), key=lambda item:(
    -elec[item]["rating"],
    elec[item]["price"],
    item
))
best_rating = srt[0]
print(best_rating)
res = products[best_rating]["rating"]
print(res)