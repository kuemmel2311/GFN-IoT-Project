#include <ArduinoJson.h>  // Include ArduinoJson library for JSON formatting
#include "ArduinoLowPower.h" // Include lowpower modes for battery operation
#include "MQ135.h" // MQ135 Library

#define MQ135_PIN A0  // Define MQ135 air quality sensor pin
#define RZERO 1       // Define RValue for MQ135 sensor
#define LDR_PIN A1    // Define LDR (Light Dependent Resistor) sensor pin

MQ135 gasSensor = MQ135(MQ135_PIN);

void setup() {
    Serial.begin(9600);  // Start serial communication with a baud rate of 9600
}

void loop() {
    // Read raw analog values from sensors
    int ldrValue = analogRead(LDR_PIN);     // Read LDR sensor (light intensity)

    // Get values from MQ135 sensor
    int mq135Raw = analogRead(MQ135_PIN); 
    float mq135R0 = gasSensor.getRZero();
    float ppm = gasSensor.getPPM();  // Approximate PPM conversion 

    // Create a JSON object to store sensor values
    StaticJsonDocument<200> jsonDoc;
    jsonDoc["LDR_RAW"] = ldrValue;         // Store LDR sensor value
    jsonDoc["MQ135_RAW"] = mq135Raw;      // Store MQ135 raw ADC value
    jsonDoc["MQ135_R0"] = mq135R0;      // Store MQ135 raw ADC value
    jsonDoc["MQ135_PPM"] = ppm;           // Store MQ135 converted PPM value

    // Convert the JSON object to a string and send it via serial
    serializeJson(jsonDoc, Serial);
    Serial.println();  // Print a newline to separate JSON outputs

    LowPower.sleep(1000); // Light sleep for 1 second
}
