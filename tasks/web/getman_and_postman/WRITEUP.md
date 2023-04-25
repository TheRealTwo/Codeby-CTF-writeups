# GETman и POSTman: Write-up #
Попадая на сайт, видим лишь это:

    Привет! Для того чтобы получить флаг, отправь запрос содержащий: GET-параметр (want_flag=YES) и POST-параметры (admin=1 и message=Hello)
    POST параметры: {}
    GET параметры: {}

Если кому-то неизвестно, то GET-параметры передаются через url: `ip:port/?param=value`.
В нашем случае ссылка будет следующей: `http://62.173.140.174:16002/?want_flag=yes`

POST-параметр можно передать через довольно многофункциональную утилиту `curl`. Ссылку вставим с уже подготовленным GET-параметром.<br/>
POST-параметры необхожимо передать в виде json-данных, указав при этом хэдер `Content-Type: application/json`. Команда будет выглядеть так:
        
        $ curl -X POST http://62.173.140.174:16002/?want_flag=YES -H "Content-Type: application/json" -d '{"admin": 1, "message": "Hello"}'

В итоге получаем следующий ответ:

    Привет! Для того чтобы получить флаг, отправь запрос содержащий: GET-параметр (want_flag=YES) и POST-параметры (admin=1 и message=Hello)
    POST параметры: {'admin': 1, 'message': 'Hello'}
    GET параметры: {'want_flag': 'YES'}
    Поздравляю! Твой флаг: CODEBY{p0st_g3t_tr0ubl3s} 
