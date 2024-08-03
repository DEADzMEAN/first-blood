import urllib.request

# Эта переменная содержит запрос к 'http://localhost:1234/'.
# Возможно, сейчас вы задаётесь вопросом о том, что такое 'http://localhost:1234'.
# localhost указывает на то, что программа работает с локальным сервером.
# 1234 - это номер порта, который вам предлагалось запомнить при настройке серверного кода.

fp = urllib.request.urlopen("http://localhost:1234/")
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Выводим содержимое файла, полученного с сервера ('index.html').

print(decodedContent)
fp.close()