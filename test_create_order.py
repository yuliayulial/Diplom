# Юлия Волкова, 11-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stend_reguest

def create_order():
    create_order_response = sender_stend_reguest.post_new_order(data.order_body)
    assert create_order_response.status_code == 201
    return create_order_response.json()["track"]

def test_create_order_track():
    track_number = create_order()
    print("Заказ создан. Номер заказа:", track_number)
    order_response = sender_stend_reguest.get_order(track_number)
    assert order_response.status_code == 200