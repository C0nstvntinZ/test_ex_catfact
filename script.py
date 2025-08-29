import requests

response = requests.get("https://catfact.ninja/facts")#Пункт 1

if response.status_code == 200:
    print("Подключение произошло успешно, Пункт 1")
    data = response.json()# Получаем словарь
    print(data)

    print(f"Пункт 2: Сколько всего фактов? {data.get('total')}")#Пункт 2
    print(f"Пункт 3: Сколько всего фактов? {data.get("per_page")}")#Пункт 3

    last_page=data.get('total')/data.get("per_page")
    if last_page % 1 != 0:
        last_page=last_page // 1
        last_page = int(last_page) + 1

response=requests.get("https://catfact.ninja/facts", {"page": last_page})
if response.status_code == 200:
    print("Подключение произошло успешно, Пункт 4")
    data = response.json()# Получаем словарь последней страницы
    print(data)
    facts = data["data"]
    short_fact=facts[0]
    for i in facts:
        if len(i["fact"])<len(short_fact["fact"]):
            short_fact=i

    print(f"Пункт 5: Самый короткий fact это {short_fact}")