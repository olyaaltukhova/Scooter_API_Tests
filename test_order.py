# Ольга Алтухова, 44-я когорта – Финальный проект. Инженер по тестированию плюс

from data import get_order_data
from order_functions import create_order, get_order_by_track

def test_create_and_get_order():
    order_data = get_order_data()

    create_response = create_order(order_data)
    assert create_response.status_code == 201, f"Ожидался 201, получен {create_response.status_code}"

    track = create_response.json().get("track")
    print(f"Заказ создан. Трек: {track}")

    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, f"Ожидался 200, получен {get_response.status_code}"

    print(f"Заказ получен по треку {track}")

if __name__ == "__main__":
    test_create_and_get_order()