# Приключения с флагом: Write-up #
Попадая на сайт, видим лишь гифку. А вот исходный код сайта содержит строку поинтереснее: `<-- part1: CODEBY{*** -->`

С html всё, теперь лезем в Javascript (main.js).<br/>
Видим интересный комментарий: `// 👇️ Change text color part2: **** on mouseout`

На очереди CSS (styles.css): `/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, part3: ****,  Safari 7+ */    `

Осталась одна часть флага, но все документы нами уже были просмотрены. Хинт наводит на мысль про файл robots.txt, так что смотрим его:

    User-agent: *
    Disallow: /

    # part4: ***}
  
У нас есть все 4 части флага, поэтому соединяем их в один флаг:
    
    CODEBY{********}

Как вам таск?
