#include <Wire.h>
#include <MPU6050_tockn.h>
#include <esp_now.h>
#include <WiFi.h>


MPU6050 mpu6050(Wire);

const int outputInterval = 50;  // 输出间隔时间，单位毫秒
unsigned long previousMillis = 0;

float accX, accY, accZ;
float gyroX, gyroY, gyroZ;
float roll = 0, pitch = 0, yaw = 0;

// esp board MAC address: C0:49:EF:12:D4:F0
uint8_t receiver_address[6] = {0xC0, 0x49, 0xEF, 0x12, 0xD4, 0xF0};

typedef struct data_struct {
  int id;
  float pitch;
  float roll;
  float yaw;
  float ax;
  float ay;
  float az;
  float wx;
  float wy;
  float wz;
} data_struct;

data_struct MyData;

esp_now_peer_info_t peerInfo;



void setup() {
  Wire.begin(18,23);//  sda scl 速率需要设置 400000UL
  Serial.begin(115200);
  
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);

  // Init Serial Monitor
  Serial.begin(115200);

  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  // esp_now_register_send_cb(OnDataSent);
  
  // Register peer
  memcpy(peerInfo.peer_addr, receiver_address, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
  
  // Add peer        
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }

}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= outputInterval) {
    previousMillis = currentMillis;

    mpu6050.update();

    accX = mpu6050.getAccX();
    accY = mpu6050.getAccY();
    accZ = mpu6050.getAccZ();
    gyroX = mpu6050.getGyroX();
    gyroY = mpu6050.getGyroY();
    gyroZ = mpu6050.getGyroZ();
  /*
    Serial.print(accX);
    Serial.print(" ");
    Serial.print(accY);
    Serial.print(" ");
    Serial.print(accZ);
    Serial.print(" ");
    Serial.print(gyroX);
    Serial.print(" ");
    Serial.print(gyroY);
    Serial.print(" ");
    Serial.println(gyroZ);
*/



    // float rollAcc = atan2(accY, accZ) * 180 / PI;
    float rollAcc = atan2(accY, sqrt(accX * accX + accZ * accZ)) * 180 / PI;
    float pitchAcc = atan2(accX, sqrt(accY * accY + accZ * accZ)) * 180 / PI;
    Serial.print(rollAcc);
    Serial.print(" ");
    Serial.print(pitchAcc);
    roll = 0.70 * (roll + gyroX * outputInterval / 1000) + 0.30 * rollAcc;
    pitch = 0.70 * (pitch + gyroY * outputInterval / 1000) + 0.30 * pitchAcc;

    Serial.print(" ");
    Serial.print(roll);
    Serial.print(" ");
    Serial.println(pitch);


    MyData.id = 1;
    MyData.pitch = pitch;
    MyData.roll = roll;


    esp_now_send(receiver_address, (uint8_t *) &MyData, sizeof(MyData));

  }
}