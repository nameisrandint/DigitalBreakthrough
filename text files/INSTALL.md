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
# Узнаем, где находтися python (windows):
where.exe python
>>> C:\Users\dmitm\AppData\Local\Programs\Python\Python39\python.exe
>>> C:\Users\dmitm\AppData\Local\Microsoft\WindowsApps\python.exe

# Переходим в папку, где хотим создать виртуальное окружение, например, с названием env_rosatom:
cd C:\competitions\
# Создаем вирт. окружение, С УКАЗАНИЕМ ПУТИ ДО НУЖНОГО Python'а:
virtualenv --python C:\Users\dmitm\AppData\Local\Programs\Python\Python39\python.exe env_rosatom
```

Запустить виртуальное окружение:
```
C:\competitions\env_rosatom\Scripts\activate.bat
# Было в терминале:
>>> C:\сompetitions\
# Стало (что значит, все команды выполняются из вирт. окружения env_rosatom_qvant):
>>> (env_rosatom_qvant) C:\competitions\
```

Ставим нужные библиотеки (т.к. запущено вирту. окружение, то всё будет ставиться в него):
```
pip install notebook
pip install --index-url https://repo.qboard.tech/ qboard-client
pip install qiskit
pip install matplotlib
```
