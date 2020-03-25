import requests, os, sys, colorama
os.system('clear')
fname = os.path.basename(__file__)
code = "Exploit"
print("""\033[36m
_____________________________________________
    _____
    /    )
---/----/----__----__----__----__----__---__-
  /    /   /___) /   ) /   ) /   ) /   ) (_ `
_/____/___(___ _(___(_/___/_(___/_/___/_(__)_
Эксплойт      [Deanons]      vk: @yra13337
                             tg: @exploitex
""")
print("""
[1] - РСЃРєР°С‚СЊ РёРЅС„РѕСЂРјР°С†РёСЋ
[2] - Р”РѕР±Р°РІРёС‚СЊ РёРЅС„РѕСЂРјР°С†РёСЋ
""")
while True:
    AorB = input("\033[35m[*]:\033[0m ")
    if AorB == '1':
        keysay=input("\033[32m[РљР»СЋС‡РµРІРѕРµ СЃР»РѕРІРѕ][#]:\033[0m ")
        try:
            print(requests.get("https://solomolopolo112.000webhostapp.com/deanons.php?code="+code+"&index="+keysay).text)
        except:
            print("\033[31mР§С‚Рѕ-С‚Рѕ РЅРµ С‚Р°Рє РїРѕС€Р»Рѕ.\033[0m")
    elif AorB == '2':
        print("РџРёС€РёС‚Рµ РёРЅС„РѕСЂРјР°С†РёСЋ РєРѕС‚РѕСЂСѓСЋ С…РѕС‚РёС‚Рµ РґРѕР±Р°РІРёС‚СЊ.")
        tex = input("\033[32m[РРЅС„РѕСЂРјР°С†РёСЏ][#]:\033[0m ")
        try:
            print("\033[31mР•СЃР»Рё Сѓ РІР°СЃ РѕС‚СЃСѓС‚СЃС‚РІСѓРµС‚ РєРѕРґ, РІР°Рј РЅР°РґРѕ Р°РІС‚РѕСЂРёР·РѕРІР°С‚СЊСЃСЏ С‚СѓС‚:\033[0m")
            print("\033[33mhttps://goo-gl.ru/66AH\033[0m")
            codes = input("\033[32m[Р’Р°С€ РєРѕРґ][#]:\033[0m ")
            print(requests.get("https://solomolopolo112.000webhostapp.com/infsave.php?pass="+codes+"&txt="+tex).text)
        except:
            print("Р§С‚Рѕ-С‚Рѕ РЅРµ С‚Р°Рє РїРѕС€Р»Рѕ.")
    elif AorB == '3':
        print("РџРёС€РёС‚Рµ РёРЅС„РѕСЂРјР°С†РёСЋ РєРѕС‚РѕСЂСѓСЋ С…РѕС‚РёС‚Рµ РґРѕР±Р°РІРёС‚СЊ.")
        tex = input("\033[32m[РРЅС„РѕСЂРјР°С†РёСЏ][#]:\033[0m ")
        try:
            print(requests.get("https://solomolopolo112.000webhostapp.com/infsave.php?i=0&txt="+tex).text)
        except:
            print("Р§С‚Рѕ-С‚Рѕ РЅРµ С‚Р°Рє РїРѕС€Р»Рѕ.")
    else:
        print("error")
