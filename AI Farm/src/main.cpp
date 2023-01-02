#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>

char ssid[] = "ASUS";
char password[] = "";
String url = "https://api.thingspeak.com/update?api_key=JF5LE1V27O8K5U11";

void setup()
{
    Serial.begin(9600);
    Serial.print("connecting to WIFI: ");
    Serial.println(ssid);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(1000);
    }
    Serial.println("WIFI connected");
}

void loop()
{
    float debug = 2.1f;
    HTTPClient http;
    String query = url + "&field1=" + debug;

    http.begin(query);
    int httpCode = http.GET();
    if (httpCode == HTTP_CODE_OK) {
        String payload = http.getString();
        Serial.print("response: ");
        Serial.println(payload);
    } else {
        Serial.print("status code: ");
        Serial.println(httpCode);
    }
    http.end();
    delay(1000);
}

