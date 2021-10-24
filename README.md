# DigitalBreakthrough
Репозиторий к цифровому прорыву.

Что мы понимаем на текущий момент:

1. Quadratic unconstrained binary optimization (QUBO) - квадратичная неограничная бинарная оптимизация - известная оптимизационная проблема
2. Цель QUBO - найти максимум или минимум функции: "N-мерный вектор на NxN матрицу коэффициентов на транспонированный этот же вектор"
3. Даны три облачных сервиса квантовых вычислений: два можно запускать бесконечно, а один *лишь трижды*. На двух дебажить, а на D-Wave прогонять готовое решение.
4. Ключ к сервисам у капитана.

## Подготовка к работе:
1. Установить библиотеки из [```requirements.txt```](requirements.txt), например:
```shell
pip install -r C:\competitions\DigitalBreakthrough\requirements.txt
# т.е. вызываем pip install с флагом -r и указываем путь к requirements.txt файлу, который лежит в склонированном репозитории
``` 
2. Помещаем ```production.yml``` от админа в папку [configs/](configs)

## Запуск скриптов:
1. Запускаем терминал windows: ```Win```+```R```, пишем ```cmd```, нажимаем OK. Переходим в папку, в котором склонирован репозиторий, например:
```shell
cd C:\competitions\DigitalBreakthrough
```

2. HELP-описание запуск [```run_example.py```](run_example.py) от Игоря с рандомной Q-матрицей. Пример запуска:
```shell
python run_example.py -h
```

Полный пример *(только после --access_key в кавычках нужно указать реальный access_key к QBOARD-платформе от нашего админа)*:
```shell
python run_example.py --access_key "123example456-of78-the9-qboard0key1"
```

## Запуск VK-бота:
1. Переходим в терминале в директорию проекта:
```shell
cd C:\competitions\DigitalBreakthrough
```

2. HELP-описание работы скрипта [```run_vk_bot.py```](run_vk_bot.py), токены для QBOARD и VK-бота берутся из YML-конфига, который указываете. 
Нужно указывать ```production.yml``` (подробнее: см. **"Подготовка к работе" пункт 2.**)
```shell
python run_vk_bot.py -h
```

Пример запуска:
```shell
python run_vk_bot.py -d -yml C:\competitions\DigitalBreakthrough\configs\production.yml
```
