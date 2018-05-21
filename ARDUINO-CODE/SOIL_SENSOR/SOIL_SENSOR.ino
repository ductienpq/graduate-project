void setup() 
{
  Serial.begin(9600);//Mở cổng Serial ở mức 9600
}
 
void loop() 
{
  int value = analogRead(A0);     // Ta sẽ đọc giá trị hiệu điện thế của cảm biến
  int percent = map(value, 0, 1023, 0, 100);
  Serial.print(percent);
  Serial.println('%');
  delay(2000);
}
