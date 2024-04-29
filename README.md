# DemonDjango

![image](https://github.com/0gl04q/DemonDjango/assets/115027096/04659de0-8da8-41b1-84ae-8aee968e683a)

## Описание

DemonDjango (специально с ошибкой) - это тестовый проект реализующий в себе демона и джанго сервер.
Сервер работает динамически засчет js/ajax и HTMX. Так же добавлен bootstrap5 для стилизации.

## Установка

1) Установить проект как пакет через `pip`

``` shell
pip install git+https://github.com/0gl04q/DemonDjango.git
```

2) Вписать приложения проекта в ``INSTALLED_APPS``

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'django_bootstrap5',
    'daemon_django_apps.api.apps.ApiConfig',
    'daemon_django_apps.info.apps.InfoConfig'
]
```
3) Добавтьте HTMX
- ``<body  hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'>``
- ``<script src="https://unpkg.com/htmx.org@1.9.4"></script>``

4) Сделать миграции 

```shell
python manage.py migrate
```

5) Дать права на исполнение срипта(демона)

```shell
chmod +x ('Укажите папку с окружением')/lib/('Укажите свою версию Python')/site-packages/daemon_django_apps/scripts/daemon_script.sh 
```
6) Создать демона

- Отрыть файл службы
```shell
sudo nano /etc/systemd/system/daemon_script.service
```
- Вставить описание службы
```
[Unit]
Description=Daemon Script 
After=multi-user.target

[Service]
Type=simple
ExecStart=/путь/до/daemon_script.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```
- Запустите демона и поставьте в автозапуск
```bash 
systemctl daemon-reload
systemctl start daemon_script.service
systemctl enable daemon_script.service
```
