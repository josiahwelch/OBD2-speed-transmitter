#include <SPI.h>
#include <LoRa.h>

void setup() {
	Serial.begin(9600);
	while (!Serial);

	//LoRa.setPins(18, 14, 26);  // NSS, RESET, DIO0 (adjust if needed)
	LoRa.setPins(16, 14, 26);  // NSS, RESET, DIO0 (adjust if needed)

	if (!LoRa.begin(915E6)) {  // Use 868E6 in Europe
		Serial.println("LoRa init failed!");
		while (1);
	}

	Serial.println("LoRa Sender");
}

void loop() {
	if (Serial.available() > 0) {
		String msg = Serial.readString();
		Serial.println("Sending from serial...");
		LoRa.beginPacket();
		LoRa.print(msg);
		LoRa.endPacket();
	}
}
