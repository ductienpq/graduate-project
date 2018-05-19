#include <DHT.h>          
#include <ArduinoJson.h>
#define DHTPIN 8
#define DHTTYPE DHT11 //Khai báo loại cảm biến, có 2 loại là DHT11 và DHT22
 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  Serial.begin(9600);
  dht.begin();         // Khởi động cảm biến
}
 
void loop() {
sendDHT11info();
  delay(1000);
}

void sendDHT11info() {
  float h = dht.readHumidity();    //Đọc độ ẩm
  float t = dht.readTemperature(); //Đọc nhiệt độ
  if (isnan(h) || isnan(t)) {
     //Serial.println("Failed to read from DHT sensor!");
     return;
  }
  // Tạo chuỗi Json để gửi lên Server
  StaticJsonBuffer<200> jsonBuffer2;
  JsonObject& root2 = jsonBuffer2.createObject();
  root2["t"] = t;
  root2["h"] = h;
  root2.printTo(Serial);
  Serial.println();
}

