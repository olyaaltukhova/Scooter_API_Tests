import requests
from endpoints import CREATE_ORDER, GET_ORDER_BY_TRACK

def create_order(order_data):
    response = requests.post(CREATE_ORDER, json=order_data)
    return response

def get_order_by_track(track):
    response = requests.get(GET_ORDER_BY_TRACK, params={"t": track})
    return response
