import asyncio
import argparse


hello_message = \
"""
  ___                                         _____       _      
 / _ \                                       /  __ \     | |     
/ /_\ \_      _____  ___  ___  _ __ ___   ___| /  \/ __ _| | ___ 
|  _  \ \ /\ / / _ \/ __|/ _ \| '_ ` _ \ / _ \ |    / _` | |/ __|
| | | |\ V  V /  __/\__ \ (_) | | | | | |  __/ \__/\ (_| | | (__ 
\_| |_/ \_/\_/ \___||___/\___/|_| |_| |_|\___|\____/\__,_|_|\___|

Awesome Powerfull Calculator

Example:
>>> 1+1
2
>>> (7 ** 2) % 5
4

Hint: Type 'exit' to exit the app
"""[1:].encode()

hello_message += b"\n>>> "




async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):

    # send hello
    writer.write(hello_message)
    await writer.drain()
    try:
        while True:
            data = await reader.readline()
            message = data.decode().strip()

            if message == "exit":
                break

            try:
                calculate = str(eval(message))  # vuln
            except Exception as f:
                calculate = str(f)

            answer = calculate.encode()
            answer += b"\n>>> "

            writer.write(answer)
            await writer.drain()

        writer.close()
        
    except Exception as f:
        print(f)
        writer.close()

async def start_service(host: str, port: int):
    service = await asyncio.start_server(handler, host, port)
    await service.serve_forever()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default="0.0.0.0")
    parser.add_argument('--port', type=int, default=31337)
    
    ConnectionInfoParsed = parser.parse_args()
    HOST = ConnectionInfoParsed.host
    PORT = ConnectionInfoParsed.port
    
    # HOST = "0.0.0.0"
    # PORT = 31337
 
    print(f"Starting tcp server on {HOST}:{PORT}")
    asyncio.run(start_service(HOST, PORT))


if __name__ == "__main__":
    main()