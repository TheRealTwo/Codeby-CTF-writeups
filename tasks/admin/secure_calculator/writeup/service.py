import asyncio
from string import ascii_lowercase
import argparse

hello_message = \
    """
  ___                                         _____       _        _____       _____ 
 / _ \                                       /  __ \     | |      / __  \     |  _  |
/ /_\ \_      _____  ___  ___  _ __ ___   ___| /  \/ __ _| | ___  `' / /'     | |/' |
|  _  \ \ /\ / / _ \/ __|/ _ \| '_ ` _ \ / _ \ |    / _` | |/ __|   / /       |  /| |
| | | |\ V  V /  __/\__ \ (_) | | | | | |  __/ \__/\ (_| | | (__  ./ /___  _  \ |_/ /
\_| |_/ \_/\_/ \___||___/\___/|_| |_| |_|\___|\____/\__,_|_|\___| \_____/ (_)  \___/ 
                                                                                     
Awesome Powerfull Calculator

Example:
>>> 1+1
2
>>> (7 ** 2) % 5
4

Devlog:
* I just blocked all ascii letters to increase security =D

Hint: Type 'exit' to exit the app
"""[1:].encode()

hello_message += b"\n>>> "


async def check_msg(msg: str):
    blacklist = ascii_lowercase
    lowered = msg.lower()
    if len(msg) > 1500:
        return False
    
    for elem in lowered:
        if elem in blacklist:
            return False
        
    return True


async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    try:
        # send hello
        writer.write(hello_message)
        await writer.drain()

        while True:
            data = await reader.readline()
            message = data.decode().strip()

            if message == "exit":
                break

            try:
                calculate = str(eval(message))  # vuln
            except Exception as f:
                calculate = str(f)

            status = await check_msg(message)
            if status:
                answer = calculate.encode()
                answer += b"\n>>> "
            else:
                answer = b"HACK ATTEMPTED!!!\n>>>"

            writer.write(answer)
            await writer.drain()

        writer.close()

    except Exception as err:
        print(err)
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
    # PORT = 31341
    print(f"Starting tcp server on {HOST}:{PORT}")
    asyncio.run(start_service(HOST, PORT))


if __name__ == "__main__":
    main()