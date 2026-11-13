# compound-interest-docker

Практична робота №5 «Контейнеризація додатків за допомогою Docker».

| Поле | Значення |
|---|---|
| Студент | Кульомін Нікіта |
| Група | З-41 |
| Номер у списку | 21 |
| Варіант | 1 (21 mod 10 = 1) — калькулятор складних відсотків |
| Мова | Python 3.12 (образ `python:3.12-slim`) |

## Що робить програма

Рахує кінцеву суму вкладу зі складними відсотками за формулою
`S = P * (1 + r/n)^(n*t)` і виводить у консоль таблицю по роках та підсумок.

Вхідні дані передаються змінними середовища:

| Змінна | Що означає | За замовчуванням |
|---|---|---|
| `SUM` | початкова сума, грн (> 0) | 10000 |
| `RATE` | річна ставка, % (≥ 0) | 10 |
| `PERIODS` | кількість років (ціле ≥ 1) | 5 |
| `COMPOUNDING` | нарахувань на рік: 1 — щороку, 12 — щомісяця | 1 |

Неправильні дані (від'ємна сума, текст замість числа) — повідомлення про помилку і код виходу 1.

## Запуск

```bash
docker build -t compound-interest .
docker run --name calc compound-interest
docker run --rm -e SUM=1000 -e RATE=5 -e PERIODS=3 compound-interest
docker run --rm -e SUM=10000 -e RATE=12 -e PERIODS=2 -e COMPOUNDING=12 compound-interest
```

Перевірка:

```bash
docker images
docker ps -a
docker logs calc
```

Прибирання:

```bash
docker rm calc
docker rmi compound-interest
```

## Перевірка результату

| Вхід | Очікувана кінцева сума |
|---|---|
| SUM=10000, RATE=10, PERIODS=5 | 16 105.10 грн |
| SUM=1000, RATE=5, PERIODS=3 | 1 157.63 грн |
| SUM=10000, RATE=12, PERIODS=2, COMPOUNDING=12 | 12 697.35 грн |
