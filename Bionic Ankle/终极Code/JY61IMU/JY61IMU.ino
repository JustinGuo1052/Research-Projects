#include <esp_now.h>
#include <WiFi.h>

#include "IMUdata.hpp"

IMUdata imu1(Serial1);
unsigned long lasttime = 0;

long ledtime = 0;
// 接收端物理地址 A0:B7:65:6C:7C:C8
// 测试板接收端地址  48:E7:29:A1:57:5C
uint8_t broadcastAddress[] = { 0x48, 0xE7, 0x29, 0xA1, 0x57, 0x5C };

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

data_struct senddata;  // 发送数据
data_struct redata;    //

unsigned char sign;
float a[3], w[3], angle[3], T;
unsigned char Re_buf[11], counter;
int datacount = 0;

esp_now_peer_info_t peerInfo;


// callback when data is sent
void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  // Serial.print("\r\nLast Packet Send Status:\t");
  // Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}

void setup() {
  // initialize serial:
  Serial.begin(115200);
  Serial1.begin(115200, SERIAL_8N1, 16, 17);
  pinMode(LED_BUILTIN, OUTPUT);

  WiFi.mode(WIFI_STA);
  // Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_register_send_cb(OnDataSent);
  // Register peer
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  // Add peer
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  if (Serial1.available())  // USART 串行接收中断
  {
    Re_buf[counter] = (unsigned char)Serial1.read();  // 不同单片机略有差异
    if (counter == 0 && Re_buf[0] != 0x55)
      return;  // 第 0 号数据不是帧头，跳过
    counter++;
    if (counter == 11)  // 接收到 11 个数据
    {
      counter = 0;  // 重新赋值，准备下一帧数据的接收
      sign = 1;
    }
  }
  if (sign) {
    sign = 0;
    if (Re_buf[0] == 0x55)  
    {
      switch (Re_buf[1]) {
        case 0x51:
          a[0] = (short(Re_buf[3] << 8 | Re_buf[2])) / 32768.0 * 16;
          a[1] = (short(Re_buf[5] << 8 | Re_buf[4])) / 32768.0 * 16;
          a[2] = (short(Re_buf[7] << 8 | Re_buf[6])) / 32768.0 * 16;
          T = (short(Re_buf[9] << 8 | Re_buf[8])) / 340.0 + 36.25;
          senddata.ax = 9.8*a[0];
          senddata.ay = 9.8*a[1];
          senddata.az = 9.8*a[2];
          datacount++;
          break;
        case 0x52:
          w[0] = (short(Re_buf[3] << 8 | Re_buf[2])) / 32768.0 * 2000;
          w[1] = (short(Re_buf[5] << 8 | Re_buf[4])) / 32768.0 * 2000;
          w[2] = (short(Re_buf[7] << 8 | Re_buf[6])) / 32768.0 * 2000;
          T = (short(Re_buf[9] << 8 | Re_buf[8])) / 340.0 + 36.25;
          senddata.wx = w[0];
          senddata.wy = w[1];
          senddata.wz = w[2];
          datacount++;
          break;
        case 0x53:
          angle[0] = (short(Re_buf[3] << 8 | Re_buf[2])) / 32768.0 * 180;
          angle[1] = (short(Re_buf[5] << 8 | Re_buf[4])) / 32768.0 * 180;
          angle[2] = (short(Re_buf[7] << 8 | Re_buf[6])) / 32768.0 * 180;
          T = (short(Re_buf[9] << 8 | Re_buf[8])) / 340.0 + 36.25;
          senddata.pitch = angle[0];
          senddata.roll = angle[1];
          senddata.yaw = angle[2];
          datacount++;
          break;
      }
    }
  }


  // imu1.updata();

  if (millis() - lasttime > 50) 
  {
    lasttime = millis();
    // Send message via ESP-NOW
    Serial.println(String(senddata.pitch)+" "+String(senddata.roll)+" "+String(senddata.ax)+" "+String(senddata.ay));
    esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *)&senddata, sizeof(senddata));

    if (result == ESP_OK) {
      // Serial.println("Sent with success");
    } else {
      Serial.println("Error sending the data");
    }
  }

  if (millis() - ledtime > 1000) {
    ledtime = millis();
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  }
}
