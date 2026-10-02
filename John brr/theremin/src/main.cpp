#include <Arduino.h>

#define red 7
#define blue 4
#define green 2

#define buzzer 8
#define photoresistor A0

void setup() {
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(photoresistor, INPUT);
  Serial.begin(9600);
}

void loop() {
  int res = analogRead(photoresistor);
  if (res < 350) {
    tone(buzzer, res);
  } else {
    noTone(buzzer);
  }
}