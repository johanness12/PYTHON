#include <Arduino.h>

#define LED_PIN 13
#define button 4

bool isOn = false;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(button, INPUT);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    String command = Serial.readString();
    command.trim();
    Serial.println("Received command: " + command);
    if(command == "ON") {
      digitalWrite(LED_PIN, HIGH);
    } else if(command == "OFF") {
      digitalWrite(LED_PIN, LOW);
    }
  }
  int but = digitalRead(button);
  if (but == 1) {
    digitalWrite(LED_PIN, LOW);
    isOn = false;
  } else {
    digitalWrite(LED_PIN, HIGH);
    isOn = true;
  }
  delay(1000);
}
