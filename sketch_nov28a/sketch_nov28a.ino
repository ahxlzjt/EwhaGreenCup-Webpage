#include <WiFi.h>         // ESP32 기본 Wi-Fi 라이브러리
#include <TinyGPS++.h>    // GPS 라이브러리
#include <HardwareSerial.h> // ESP32 하드웨어 시리얼

#define RXPin 16   // GPS TX → ESP32 RX (핀 16)
#define TXPin 17   // GPS RX → ESP32 TX (핀 17)

const char* ssid = "iPhone";
const char* password = "42849929";
const char* serverUrl = "http://172.20.10.3:8080/position/";

TinyGPSPlus gps;
HardwareSerial SerialGPS(2);

void setup() {
  Serial.begin(115200);        
  SerialGPS.begin(9600, SERIAL_8N1, RXPin, TXPin); 

  WiFi.begin(ssid, password);
  Serial.println("Wi-Fi 연결 중...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi 연결 완료!");
  Serial.print("ESP32 IP 주소: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  while (SerialGPS.available() > 0) {
    gps.encode(SerialGPS.read());

    if (gps.location.isUpdated()) {
      Serial.print("위도: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("경도: ");
      Serial.println(gps.location.lng(), 6);
    } else {
      // 데이터가 없을 경우 빈칸 출력
      Serial.println("GPS 데이터 없음: 위도: ---, 경도: ---");
    }
  }

  delay(5000); // 5초 대기
}

void sendGpsData(float latitude, float longitude) {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;

    if (client.connect("172.20.10.3", 8080)) {
      String request = "GET /position/?lat=" + String(latitude, 6) + "&lng=" + String(longitude, 6) + " HTTP/1.1\r\n";
      request += "Host: 172.20.10.3\r\n";
      request += "Connection: close\r\n\r\n";

      client.print(request);
      client.stop();
      Serial.println("GPS 데이터 전송 완료: ");
      Serial.println(request);
    } else {
      Serial.println("서버 연결 실패");
    }
  } else {
    Serial.println("Wi-Fi 연결 끊김");
  }
}
