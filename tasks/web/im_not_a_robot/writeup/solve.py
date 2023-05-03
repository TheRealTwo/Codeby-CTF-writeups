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