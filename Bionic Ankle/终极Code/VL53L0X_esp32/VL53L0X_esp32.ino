#include <esp_now.h>
#include <WiFi.h>
#include <Wire.h>
#include <VL53L0X.h>

// esp board MAC address: C0:49:EF:12:D4:F0

const int outputInterval = 50;  // 输出间隔时间，单位毫秒
unsigned long previousMillis = 0;
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

VL53L0X sensor_0;
VL53L0X sensor_1;
VL53L0X sensor_2;
VL53L0X sensor_3;
VL53L0X sensor[4] = {sensor_0, sensor_1, sensor_2, sensor_3};

const int num = 4;
const int length = 100;
const int width = 60;
const int pi = 3.1415;

struct two {
  double first;
  double second;
};

void PCA9548A(uint8_t bus) {
  Wire.beginTransmission(0x70);
  Wire.write(1 << bus);
  Wire.endTransmission();
}

double Find_angle(double d1, double d2, int length) {
  double side = d1 - d2;
  return atan2(side, length);
}

two Find_PR(int LU, int LD, int RU, int RD) {
  double h1 = (LU + RU) / 2;
  double h2 = (LD + RD) / 2;

  double v1 = (LU + LD) / 2;
  double v2 = (RU + RD) / 2;
  /*
  Serial.print(h1);
  Serial.print(" ");
  Serial.print(h2);
  Serial.print(" ");
  Serial.print(v1);
  Serial.print(" ");
  Serial.println(v2);
  */
  two ans = {Find_angle(h1, h2, length), Find_angle(v1, v2, width)};

  return ans;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Wire.begin(18, 23);
  delay(100);
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


  for (int i = 0; i < num; i++) {
    PCA9548A(i);
    sensor[i].setTimeout(500);
    if (!sensor[i].init()) {
      while (true) {
        Serial.println(i);
        if (sensor[i].init()) {break;}
      }
    }
    sensor[i].startContinuous();
  }


}

const int points = 7;
int window[4][points];
int num_data = 0;

void loop() {
  int d[4];
  bool ok = true;
  for (int i = 0; i < num; i++) {
    PCA9548A(i);
    
    if (sensor[i].timeoutOccurred()) {
      ok = false;
    }
    else {
      d[i] = sensor[i].readRangeContinuousMillimeters();
      if (d[i] == 8190) {
        ok = false;
      }
    }
  }

  if (ok) {
    if (num_data < points) {
      for (int i = 0; i < 4; i++) {
        window[i][num_data] = d[i];
      }
      num_data++;
    }

    else {
      int average[4];

      for (int i = 0; i < 4; i++) {
        average[i] = window[i][0];
      }
      for (int i = 0; i < 4; i++) {
        for (int j = 1; j < points; j++) {
          average[i] += window[i][j];
          window[i][j - 1] = window[i][j];
        }
      }

      for (int i = 0; i < 4; i++) {
        window[i][points - 1] = d[i];
        average[i] /= points;
      }

      two angles_1 = Find_PR(d[1], d[3], d[0], d[2]);
      two angles_2 = Find_PR(average[1], average[3], average[0], average[2]);
      
      Serial.print(angles_1.first);
      Serial.print(" ");
      Serial.print(angles_1.second);
      Serial.print(" ");
      Serial.print(angles_2.first);
      Serial.print(" ");
      Serial.println(angles_2.second);
    }
  }
  


  



  /*
  if (ok) {
    two angles = Find_PR(d[1], d[3], d[0], d[2]);
    Serial.print(angles.first);
    Serial.print(" ");
    Serial.println(angles.second);
    
  }
  */






















  /*
  MyData.id = 1;
  MyData.pitch = angles.second;
  MyData.roll = angles.first;

  esp_now_send(receiver_address, (uint8_t *) &MyData, sizeof(MyData));
  */



}
