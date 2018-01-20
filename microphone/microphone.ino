int MicPin = A0;                     //pin for mic
int sirenPin = 11;                   //pin for LED
int MicValue1 = 0;                   //store mic reading
int MicValue2 = 0;                   //store mic reading

void setup(){
  pinMode(sirenPin, OUTPUT);
  pinMode(MicPin, INPUT);
  Serial.begin(9600);               //tests input value - initialize serial
}

void loop(){
  MicValue1 = analogRead(MicPin);   //read pin
  Serial.println(MicValue1);
  delay(1);                      //debug
  MicValue2 = analogRead(MicPin);
  Serial.println(MicValue2);

  //conditional -- set off LED
  if(MicValue2-MicValue1>160){        //test sensitivity -- 
    digitalWrite(sirenPin, HIGH);
    delay(2000);
    digitalWrite(sirenPin, LOW);
  }
}
