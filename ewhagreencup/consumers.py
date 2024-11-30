import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("location_group", self.channel_name)
        await self.accept()
        print("WebSocket 연결 성공")  # 디버깅용 로그 추가

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("location_group", self.channel_name)
        print("WebSocket 연결 해제")  # 디버깅용 로그 추가

    async def send_location(self, event):
        latitude = event['latitude']
        longitude = event['longitude']
        print(f"WebSocket으로 전송됨: 위도={latitude}, 경도={longitude}")  # 디버깅용 로그 추가
        await self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude': longitude
        }))

