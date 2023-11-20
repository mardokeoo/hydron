#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int white = 7;
int yellow = 8;
int green = 11;
int blue = 12;

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  pinMode(white, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.backlight();
}

void loop() {
  int sensor = analogRead(A0);
  Serial.println(sensor);

  if (sensor <= 10) {
    digitalWrite(white, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    digitalWrite(blue, LOW);
    lcd.clear();
    lcd.print("level:Nulo");
    delay(1000);
  } else if (sensor <= 150) {
    digitalWrite(white, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    digitalWrite(blue, LOW);
    lcd.clear();
    lcd.print("level:Nulo");
    delay(1000);
  } else if (sensor > 150 && sensor <= 250) {
    digitalWrite(yellow, HIGH);
    digitalWrite(white, LOW);
    digitalWrite(green, LOW);
    digitalWrite(blue, LOW);
    lcd.clear();
    lcd.print("level:Medio!");
    delay(1000);
  } else if (sensor > 250 && sensor <= 300) {
    digitalWrite(green, HIGH);
    digitalWrite(white, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(blue, LOW);
    lcd.clear();
    lcd.print("level: alto!");
    delay(1000);
  } else if (sensor > 300) {
    digitalWrite(blue, HIGH);
    digitalWrite(white, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(green, LOW);
    lcd.clear();
    lcd.print("level: muy alto !");
    delay(1000);
  }
}
