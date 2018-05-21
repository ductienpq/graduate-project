#include <SoftwareSerial.h>
#include <string.h>

#define LED 12

//--------------------------RELAY PIN
#define PORT1_RELAY 22
#define PORT2_RELAY 24
#define PORT3_RELAY 26
#define PORT4_RELAY 28

#define PORT5_RELAY 30
#define PORT6_RELAY 32
#define PORT7_RELAY 34
#define PORT8_RELAY 36



//-----------------------------------
#define low HIGH
#define high LOW

static const uint32_t Baud = 9600;

void setup() {
  Serial.begin(Baud);
  pinMode(LED,OUTPUT);

 //-----------------------RELAY PIN 
 pinMode(PORT1_RELAY,OUTPUT);
 pinMode(PORT2_RELAY,OUTPUT);
 pinMode(PORT3_RELAY,OUTPUT);
 pinMode(PORT4_RELAY,OUTPUT); 
 pinMode(PORT5_RELAY,OUTPUT);
 pinMode(PORT6_RELAY,OUTPUT);
 pinMode(PORT7_RELAY,OUTPUT);
 pinMode(PORT8_RELAY,OUTPUT); 
 
 digitalWrite(PORT1_RELAY,low);  
 digitalWrite(PORT2_RELAY,low);  
 digitalWrite(PORT3_RELAY,low);    
 digitalWrite(PORT4_RELAY,low);  
 digitalWrite(PORT5_RELAY,low);  
 digitalWrite(PORT6_RELAY,low);  
 digitalWrite(PORT7_RELAY,low);    
 digitalWrite(PORT8_RELAY,low);  

 Serial.begin(9600);

  digitalWrite(LED,HIGH);
  delay(1000);
  digitalWrite(LED,LOW);
  
}
String temp="";
void loop() {
digitalWrite(PORT1_RELAY,high);
delay(2000);
digitalWrite(PORT2_RELAY,high);
delay(2000);
digitalWrite(PORT3_RELAY,high);
delay(2000);
digitalWrite(PORT4_RELAY,high);
delay(2000);

digitalWrite(PORT1_RELAY,low);
delay(2000);
digitalWrite(PORT2_RELAY,low);
delay(2000);
digitalWrite(PORT3_RELAY,low);
delay(2000);
digitalWrite(PORT4_RELAY,low);
delay(2000);
}



