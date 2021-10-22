Установить pip:
```
python3 get-pip.py
```

Установить библиотеку для создания виртуального окружения:

```
pip install virtualenv
```

Создаем виртуальное окружение в нужной нам папке, например, вирт. окружение названием ```rosatom_env``` внутри папки ```C:\competitions\```

```
cd C:\competitions\
virtualenv rosatom_env
```

Запустить виртуальное окружение:
```
C:\competitions\rosatom_env\Scripts\activate.bat
```

Ставим нужные библиотеки в запущенное виртуальное окружение:
```
pip install notebook
pip install numpy
pip install --index-url https://repo.qboard.tech/ qboard-client
```
