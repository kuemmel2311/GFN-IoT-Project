#include <ArduinoJson.h>  // Include ArduinoJson library for JSON formatting

#define LDR_PIN A1    // Define LDR (Light Dependent Resistor) sensor pin
#define MQ135_PIN A0  // Define MQ135 air quality sensor pin

void setup() {
    Serial.begin(9600);  // Start serial communication with a baud rate of 9600
}

void loop() {
    // Read raw analog values from sensors
    int ldrValue = analogRead(LDR_PIN);     // Read LDR sensor (light intensity)
    int mq135Raw = analogRead(MQ135_PIN);   // Read MQ135 sensor (air quality raw value)

    // Convert MQ135 raw value to voltage (for calculations)
    float voltage = mq135Raw * (5.0 / 1023.0); // Convert ADC value (0-1023) to voltage (0-5V)
    
    // Calculate sensor resistance using voltage divider formula
    float RL = 10.0;  // Load resistor in kΩ (check your module specs!)
    float RS = (5.0 - voltage) / voltage * RL;  // Calculate RS using the load resistor
    // Define R0 (calibration value) - This needs to be set correctly for accurate results
    float R0 = 9.83;  // Replace with your own calibrated R0 value

    // Calculate approximate PPM (air quality value), source by chatgpt, i don't know how accurate it is
    float ppm = 116.602 * pow((RS / R0), -2.5);  // Approximate PPM conversion 

    // Create a JSON object to store sensor values
    StaticJsonDocument<200> jsonDoc;
    jsonDoc["LDR_RAW"] = ldrValue;         // Store LDR sensor value
    jsonDoc["MQ135_RAW"] = mq135Raw;      // Store MQ135 raw ADC value
    jsonDoc["MQ135_PPM"] = ppm;           // Store MQ135 converted PPM value

    // Convert the JSON object to a string and send it via serial
    serializeJson(jsonDoc, Serial);
    Serial.println();  // Print a newline to separate JSON outputs

    delay(1000);  
}
