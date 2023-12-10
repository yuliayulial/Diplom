import configuration
import requests
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH,
                         json = body)

# Получение данных о заказе по номеру трекера
def get_order(track_number):
    return requests.get(
        configuration.BASE_URL + configuration.GET_ORDER_PATH,
        params = { 't': track_number }
    )