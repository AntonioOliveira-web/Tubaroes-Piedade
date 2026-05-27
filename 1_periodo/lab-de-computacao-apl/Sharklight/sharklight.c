// Esse código foi feito através do Arduino IDE no Linux.
// É necessário que você baixe a biblioteca IRremote para o cófigo funcionar.

#include <IRremote.h>

#define PIR_PIN 4
#define IR_PIN 11
#define LED_PIN 10

IRrecv irrecv(IR_PIN);

bool luz_lig = false;
unsigned long ult_mov = 0;
const long temp_apagar = 3000;

void setup() {
    Serial.begin(9600);
    pinMode(PIR_PIN, INPUT);
    pinMode(LED_PIN, OUTPUT);
    irrecv.enableIRIn();
    Serial.println("Iniciando...");
}

void loop() {
    if (digitalRead(PIR_PIN) == HIGH) {
        ult_mov = millis();

        if (!luz_lig) {
            luz_lig = true;
            digitalWrite(LED_PIN, LOW);
        }
    }

    if (luz_lig && (millis() - ult_mov >= temp_apagar)) {
        luz_lig = false;
        digitalWrite(LED_PIN, HIGH);
    }
}
