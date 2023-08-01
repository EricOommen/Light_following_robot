void setup() {
pinMode(12,INPUT);  
pinMode(11,INPUT);
 
pinMode(7,OUTPUT);  
pinMode(6,OUTPUT);
pinMode(5,OUTPUT);
pinMode(4,OUTPUT);
}

void loop() {
  if(digitalRead(12) == 0 && digitalRead(11) == 0){
    Stop();
    delay(10);
  }
  else if(digitalRead(12) == 0 && digitalRead(11) == 1){
    right();
    delay(10);
  }
  else if(digitalRead(12) == 1 && digitalRead(11) == 0){
    left();
    delay(10);
  }
  else if(digitalRead(12) == 1 && digitalRead(11) == 1){
    forward();
    delay(10);
  }
}
  
void forward(){
  digitalWrite(7,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(5,HIGH); 
  digitalWrite(4,LOW);
  
}
void backword(){
  digitalWrite(7,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(5,LOW);
  digitalWrite(4,HIGH);  
}
void left(){
  digitalWrite(7,LOW);
  digitalWrite(6,HIGH);
  digitalWrite(5,HIGH);
  digitalWrite(4,LOW);  
}
void right(){
  digitalWrite(7,HIGH);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
  digitalWrite(4,HIGH);  
}
void Stop(){
  digitalWrite(7,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
  digitalWrite(4,LOW);

}