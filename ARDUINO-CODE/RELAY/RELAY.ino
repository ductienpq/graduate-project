#include <SoftwareSerial.h>
#include <string.h>

#define LED 12

//--------------------------RELAY PIN
#define PORT1_RELAY 4
#define PORT2_RELAY 5
#define PORT3_RELAY 6
#define PORT4_RELAY 7

//---------------State Control Relay
#define port1_Relay_ON    '1'
#define port1_Relay_OFF   '0'

#define port2_Relay_ON    '1'
#define port2_Relay_OFF   '0'

#define port3_Relay_ON    '1'
#define port3_Relay_OFF   '0'

#define port4_Relay_ON    '1'
#define port4_Relay_OFF   '0'

char port1_STT='0';
char port2_STT='0';
char port3_STT='0';
char port4_STT='0';
//-----------------------------------
#define low HIGH
#define high LOW

bool state_PORT1=false;
bool state_PORT2=false;
bool state_PORT3=false;
bool state_PORT4=false;

static const uint32_t Baud = 9600;
unsigned long previousMillis = 0;
long t = 5000;

bool Debug=false;

String port1_Name="PORT 1";
String port2_Name="PORT 2";
String port3_Name="PORT 3";
String port4_Name="PORT 4";
void setup() {
  //Serial.begin(Baud);
  pinMode(LED,OUTPUT);

 //-----------------------RELAY PIN 
 pinMode(PORT1_RELAY,OUTPUT);
 pinMode(PORT2_RELAY,OUTPUT);
 pinMode(PORT3_RELAY,OUTPUT);
 pinMode(PORT4_RELAY,OUTPUT); 
 
 digitalWrite(PORT1_RELAY,low);  
 digitalWrite(PORT2_RELAY,low);  
 digitalWrite(PORT3_RELAY,low);    
 digitalWrite(PORT4_RELAY,low);  

 Serial.begin(9600);

  digitalWrite(LED,HIGH);
  delay(1000);
  digitalWrite(LED,LOW);
  
}
String temp="";
void loop() {
    if (millis() - previousMillis > t) {
     previousMillis = millis();
  }
  

   if(Serial.available() > 0){
   // Read from serial monitor and send over UM402
    String input = Serial.readString();
    Serial.flush();
    input.trim();
    char s[10];
    
  for (byte len = 1;len<=input.length()+1; len++){    input.toCharArray(s,len);}
      relay_Control(s);
   }
}

void control_Port(byte port, String portname, byte _stt, bool debug=false){
  byte stt=low;
  if (_stt=='1') stt=high;
  digitalWrite(port,stt);
  if (debug) Serial.println("[RELAY ] "+portname+" ON");  
 }  

void relay_Control(char *input){
  //Serial.println("SEND:"+String(input));
  bool debug=false;
  
  //------------------PORT 1  
  if (input[0]==port1_Relay_ON)      {     if (input[0]!=port1_STT){      port1_STT=input[0]; control_Port(PORT1_RELAY,port1_Name,port1_STT,debug);}}    
  else if (input[0]==port1_Relay_OFF){     if (input[0]!=port1_STT){      port1_STT=input[0]; control_Port(PORT1_RELAY,port1_Name,port1_STT,debug);}}

  //------------------PORT 2
  if (input[1]==port1_Relay_ON)      {     if (input[1]!=port2_STT){      port2_STT=input[1]; control_Port(PORT2_RELAY,port2_Name,port2_STT,debug);}}
  else if (input[1]==port2_Relay_OFF){     if (input[1]!=port2_STT){      port2_STT=input[1]; control_Port(PORT2_RELAY,port2_Name,port2_STT,debug);}}
  
  //------------------PORT 3  
  if (input[2]==port3_Relay_ON)      {     if (input[2]!=port3_STT){      port3_STT=input[2]; control_Port(PORT3_RELAY,port3_Name,port3_STT,debug);}}    
  else if (input[2]==port3_Relay_OFF){     if (input[2]!=port3_STT){      port3_STT=input[2]; control_Port(PORT3_RELAY,port3_Name,port3_STT,debug);}}

  //------------------PORT 4
  if (input[3]==port4_Relay_ON)      {     if (input[3]!=port4_STT){      port4_STT=input[3]; control_Port(PORT4_RELAY,port4_Name,port4_STT,debug);}}
  else if (input[3]==port4_Relay_OFF){     if (input[3]!=port4_STT){      port4_STT=input[3]; control_Port(PORT4_RELAY,port4_Name,port4_STT,debug);}}

  }

bool checkPort(byte port){
  if(digitalRead(port)) return true;
  return false;
  }
 

      

