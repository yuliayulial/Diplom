### Тест на проверку, что по треку заказа можно получить данные о заказе в Яндекс Самокат
+ для запуска тестов установить пакеты pytest и requests


+ в файле  [configuration.py](configuration.py) в переменную **BASE_URL** 
указать адрес стенда


+ запросы хранятся в файлах [data.py](data.py), [sender_stend_reguest.py](sender_stend_reguest.py)


+ тест находится в файле [test_create_order.py](test_create_order.py), запуск теста выполняется командой **pytest**