char serialData;

void setup() {
  // put your setup code here, to run once:
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == '1')
    {
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
    }
    else if(serialData == '0')
    {
      digitalWrite(13, HIGH);
      digitalWrite(12, LOW);
    }
    else if(serialData == '2')
    {
      digitalWrite(13, HIGH);
      digitalWrite(12, HIGH);
    }
    
  }

}
