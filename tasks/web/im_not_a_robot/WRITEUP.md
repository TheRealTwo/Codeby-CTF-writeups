# Я не робот!: Write-up #
Попадая на сайт, видим незамысловатую схему проверки капчи. Просят решить что-то зашифрованное, что сильно смахивает на `base64`, особенно если в конце будет `=`. Смторим, что это такое:

    $ echo "eCA9IDM2NyArIDk2OA==" | base64 -d
    x = 367 + 968

Судя по всему, нас просят посчитать x. Считаем и вводим число:

    [+] Correct! Solve: eCA9IDYyMyArIDc4NA== (1/50)

И так 50 раз. Ручками это делать уважающий себя человек никогда не станет, так что автоматизируем это дело. В javascript видим подключение через `ws`, 
так что это можно сделать на Питуне, через либу `websockets (pip3 install websockets)`:

```python3
import websocket
import base64

ws = websocket.WebSocket()
ws.connect("ws://62.173.140.174:16011/ws")
data = ws.recv()
while "CODEBY" not in data:
	data = data.split()
	if data[-1].startswith("("):
		data = data[:-1]
	data = str(base64.b64decode(data[-1]))[2:-1]
	ans = str(eval(data[4:]))
	ws.send(ans)
	data = ws.recv()
	print(data)
```

    [!] FLAG: CODEBY{****************}
