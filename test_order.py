import requests

BASE_URL = "https://88e64e5d-96ce-4308-b5b5-3d4925acbc94.serverhub.praktikum-services.ru"

def test_create_and_get_order():
    order_data = {
        "firstName": "Ольга",
        "lastName": "Зима",
        "address": "ул. Центральная, 1",
        "metroStation": 4,
        "phone": "+79001234567",
        "rentTime": 1,
        "deliveryDate": "2026-07-12",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }
    
    # 1. Выполняем запрос на создание заказа
    create_response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
    assert create_response.status_code == 201, f"Ожидался 201, получен {create_response.status_code}"
    
    # 2. Сохраняем номер трека заказа
    track = create_response.json().get("track")
    print(f"Заказ создан. Трек: {track}")
    
    # 3. Выполняем запрос на получение заказа по треку заказа
    get_response = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
    
    # 4. Проверяем, что код ответа равен 200
    assert get_response.status_code == 200, f"Ожидался 200, получен {get_response.status_code}"
    
    print(f"Заказ получен по треку {track}")

if __name__ == "__main__":
    test_create_and_get_order()