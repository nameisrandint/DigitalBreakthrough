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
# Узнаем, где находится python (для windows):
where.exe python
>>> C:\Users\dmitm\AppData\Local\Programs\Python\Python37\python.exe
>>> C:\Users\dmitm\AppData\Local\Programs\Python\Python38\python.exe
>>> C:\Users\dmitm\AppData\Local\Programs\Python\Python39\python.exe
>>> C:\Users\dmitm\AppData\Local\Microsoft\WindowsApps\python.exe
# Копируем путь, например, от Python39 версии

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
# Стало (что значит, все команды выполняются из вирт. окружения env_rosatom):
>>> (env_rosatom) C:\competitions\
```

Переходим в папку, в которую хотим клонировать репозиторий. Клонируем репозиторий в папку, например, с названием ```rosatom_qvant``:
```shell
cd C:\сompetitions\
git clone https://github.com/nameisrandint/DigitalBreakthrough.git rosatom_qvant
# После этого появится папка с кодом репозитория внутри C:\сompetitions\rosatom_qvant\  
```

Ставим нужные библиотеки (т.к. запущено вирт. окружение, то всё будет ставиться в него):
```
# Установить нужные python-библиотеки из requirements.txt файла:
pip install -r C:\competitions\rosatom_qvant\requirements.txt
# Ставим qboard:
pip install --index-url https://repo.qboard.tech/ qboard-client

# Далее добавляем созданное виртуальное окружение в jupyter notebook (после --name= указывается название вирт. окружения):
python -m ipykernel install --name=env_rosatom
```

## Starting Jupyter Notebook:

```
# Запускаем в командной строке:
jupyter notebook --ip 0.0.0.0 --port 8090 --no-browser
# Появится что-то вроде:
>>> [I 16:36:15.219 NotebookApp] Writing notebook server cookie secret to C:\Users\dmitm\AppData\Roaming\jupyter\runtime\notebook_cookie_secret
>>> [I 16:36:16.013 NotebookApp] Serving notebooks from local directory: C:\Competitions\rosatom_qvant
>>> [I 16:36:16.013 NotebookApp] Jupyter Notebook 6.4.5 is running at:
>>> [I 16:36:16.013 NotebookApp] http://DESKTOP-AD09534:8090/?token=405d536b0db8ccad1feaf45750fd6962ea388c168e748424
>>> [I 16:36:16.013 NotebookApp]  or http://127.0.0.1:8090/?token=405d536b0db8ccad1feaf45750fd6962ea388c168e748424
>>> [I 16:36:16.013 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
>>> [C 16:36:16.043 NotebookApp]
>>> 
>>>     To access the notebook, open this file in a browser:
>>>         file:///C:/Users/dmitm/AppData/Roaming/jupyter/runtime/nbserver-24348-open.html
>>>     Or copy and paste one of these URLs:
>>>         http://DESKTOP-K541JIQ:8090/?token=405d536b0db8ccad1feaf45750fd6962ea388c168e748424
>>>      or http://127.0.0.1:8090/?token=405d536b0db8ccad1feaf45750fd6962ea388c168e748424
# Rопируем ссылку из вывделенных сообщений. В данном случае: 
# http://127.0.0.1:8090/?token=405d536b0db8ccad1feaf45750fd6962ea388c168e748424
# и вставляем её в бразуере

# Откроется WEB UI. Выбираем в нём .ipynb файл. Меняем в нём вирт. окружение: Kernel -> Change
```