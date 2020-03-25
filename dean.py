import requests, os, sys, colorama
os.system('clear')
fname = os.path.basename(__file__)
code = "termux_lab"
print("""\033[36m
_____________________________________________
    _____
    /    )
---/----/----__----__----__----__----__---__-
  /    /   /___) /   ) /   ) /   ) /   ) (_ `
_/____/___(___ _(___(_/___/_(___/_/___/_(__)_
��������      [Deanons]      vk: @yra13337
                               tg: @exploitex
""")
print("""
[1] - Искать информацию
[2] - Добавить информацию
""")
while True:
    AorB = input("\033[35m[*]:\033[0m ")
    if AorB == '1':
        keysay=input("\033[32m[Ключевое слово][#]:\033[0m ")
        try:
            print(requests.get("https://solomolopolo112.000webhostapp.com/deanons.php?code="+code+"&index="+keysay).text)
        except:
            print("\033[31mЧто-то не так пошло.\033[0m")
    elif AorB == '2':
        print("Пишите информацию которую хотите добавить.")
        tex = input("\033[32m[Информация][#]:\033[0m ")
        try:
            print("\033[31mЕсли у вас отсутствует код, вам надо авторизоваться тут:\033[0m")
            print("\033[33mhttps://goo-gl.ru/66AH\033[0m")
            codes = input("\033[32m[Ваш код][#]:\033[0m ")
            print(requests.get("https://solomolopolo112.000webhostapp.com/infsave.php?pass="+codes+"&txt="+tex).text)
        except:
            print("Что-то не так пошло.")
    elif AorB == '3':
        print("Пишите информацию которую хотите добавить.")
        tex = input("\033[32m[Информация][#]:\033[0m ")
        try:
            print(requests.get("https://solomolopolo112.000webhostapp.com/infsave.php?i=0&txt="+tex).text)
        except:
            print("Что-то не так пошло.")
    else:
        print("error")
