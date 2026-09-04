#include <esp_now.h>
#include <WiFi.h>
#include  "UartDataRx.hpp"

/*******roll PID control 角度*******/
  // float kp = 10;
  // float ki = 0.1;
  float kp = 45;
  float ki = 0.6;
  float kd = -0.06;
  float last_err;
  float err_all;
/*******pitch PID control 角度*******/
  float p_kp = 30;
  float p_ki = 0.3;
  float p_kd = -0.04;
  float err_all2;
  float P_last_err;

UartDataRx uart(Serial);

esp_now_peer_info_t peerInfo;
// callback when data is sent

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

data_struct board0;
data_struct board1;

data_struct board_struct[2] = {board0, board1};


// Create a data_struct called myData
  data_struct myData ;
// callback function that will be executed when data is received
void OnDataRecv(const uint8_t * mac_addr, const uint8_t *incomingData, int len) {
  char macStr[18];
  // Serial.print("Packet received from: ");
  snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x",
           mac_addr[0], mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
  // Serial.println(macStr);
  memcpy(&myData, incomingData, sizeof(myData));
  board_struct[myData.id].pitch = myData.pitch;
  board_struct[myData.id].roll = myData.roll;
}

data_struct myData2;



//电机控制中的定制参数与数组以及变量 
//定义一个都是八位数据类型的数组  用来存放数据
float angle1 = 0.0;
float angle2 = 0.0;
float roll_PID_angle = 0.0;
float pitch_PID_angle = 0.0;
uint8_t read_datebuffer[20] = {0};
uint8_t senddate[10]={0};
uint8_t sendvdate[10]={0};
uint32_t receivedData ;
float accelroll = 0.0;

float out[2] = {};

// esp board MAC address: C0:49:EF:12:D4:F0
void setup() {
  Serial.begin(115200);    //初始化硬件串口
  Serial2.begin(115200);    //初始化硬件串口
  WiFi.mode(WIFI_STA);
  //Init ESP-NOW
  if (esp_now_init() != ESP_OK) {
    // Serial.println("Error initializing ESP-NOW");
    return;
  }
  // 
  esp_now_register_recv_cb(OnDataRecv);
  // Register peer
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  // Add peer
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    // Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  float set_pitch = 0;
  float set_roll = 0;

  uart.getdata();
  float roll_foot = board_struct[0].roll;
  float pitch_foot = board_struct[0].pitch;

  float roll_ground = board_struct[1].roll;
  float pitch_ground = board_struct[1].pitch;
  // pitch -10, 20
  // roll -10, 20
  int lower_bound = -5;
  int upper_bound = 10;
  if (pitch_ground > upper_bound) {
    pitch_ground = upper_bound;
  }
  else if (pitch_ground < lower_bound) {
    pitch_ground = lower_bound;
  }

  if (roll_ground > upper_bound) {
    roll_ground = upper_bound;
  }
  else if (roll_ground < lower_bound) {
    roll_ground = lower_bound;
  }
  set_pitch = pitch_ground;
  set_roll = roll_ground;
  
  PID_total(roll_foot, pitch_foot, set_pitch, set_roll);
  Serial.print(roll_foot);
  Serial.print("    ");
  Serial.print(pitch_foot);
  Serial.print("    ");
  
  Serial.print(roll_ground);
  Serial.print("    ");
  Serial.print(pitch_ground);
  Serial.println(" "); 
}

//roll PID 控制系统封装
float PID_control (float now_date,float set_date )
{
  float err = set_date - now_date;
  err_all = err + err_all;

  if (err_all > 1000) err_all = 1000;
  if (err_all < -1000) err_all = -1000;
  float P_OUT = kp * err;
  float I_OUT = ki * err_all;
  float D_OUT = kd * (err - last_err);
  last_err = err;
  float all_out = P_OUT + I_OUT + D_OUT;
  if (all_out >1200) all_out = 1200;
  if (all_out < -1200) all_out = -1200;
  return all_out;
}

//pitch PID 控制系统封装
float PID_control2 (float now_date2,float set_date2)
{
  float err2 = set_date2 - now_date2;
  err_all2 = err2 + err_all2;
  if (err_all2 > 1000) err_all2 = 1000;
  if (err_all2 < -1000) err_all2 = -1000;
  float P_OUT2 = p_kp * err2;
  float I_OUT2= p_ki * err_all2;
  float D_OUT2 = p_kd * (err2 - P_last_err);
  P_last_err = err2;
  float all_out2 = P_OUT2 + I_OUT2 + D_OUT2;
  if (all_out2 > 1200) all_out2 = 1200;
  if (all_out2 < -1200) all_out2 = -1200;
  return all_out2;
 
}

void PID_total (float roll, float pitch, float set_pitch, float set_roll) {
  roll_PID_angle = PID_control(roll, set_roll);
  pitch_PID_angle = PID_control2(pitch, set_pitch);
  angle_increase_send(1,-roll_PID_angle + pitch_PID_angle); 
  delay(10); 
  angle_increase_send(2,+roll_PID_angle + pitch_PID_angle); 
  delay(10);
}



void send(int ID,int64_t angle,bool dir)
{
  senddate[0]=0x3E;
  senddate[1]=0xA5;
  senddate[2]=ID;//电机ID
  senddate[3]=0x04;
  senddate[4]=senddate[0]+senddate[1]+senddate[2]+senddate[3];
  
  senddate[5]=dir;//转动方向  0顺 1逆
  senddate[6] = (uint8_t)(angle & 0xFF);//数据低八位
  senddate[7] = (uint8_t)((angle >> 8) & 0xFF);//数据高八位
  senddate[8] = 0x00;
  senddate[9]=senddate[5]+senddate[6]+senddate[7]+senddate[8];
  Serial2.write(senddate,10);
}

float single_read(int ID)  //电机单圈角度读取
{
  uint8_t readdate[5] = {0};
  uint8_t temp = 0;
  readdate[0] = 0x3E;
  readdate[1] = 0x94;
  readdate[2] = ID;
  readdate[3] = 0x00;
  readdate[4] = readdate[0] + readdate[1] + readdate[2] + readdate[3];
  Serial2.write(readdate,5);
  //数据接收
  if (Serial2.available() >= sizeof(read_datebuffer)+3) {
    Serial2.readBytes((uint8_t *)&read_datebuffer, sizeof(read_datebuffer));  // 读取数据到接收数据缓冲区中
  }
  for (int i = 0; i < 11; i++) {
    if (read_datebuffer[i] == 0x3E) {
      temp = read_datebuffer[i] + read_datebuffer[i + 1] + read_datebuffer[i + 2] + read_datebuffer[i + 3];
      if (read_datebuffer[i + 4] == temp) {
        receivedData = (uint32_t)read_datebuffer[i + 5] | ((uint32_t)read_datebuffer[i + 6] << 8) | ((uint32_t)read_datebuffer[i + 7] << 16) | ((uint32_t)read_datebuffer[i + 8] << 24);
        float readangle = (float)receivedData / 100.00;
        read_datebuffer[20] = {0};
        delay(10);
        return readangle;
        
      }
    }
  }

  Serial.println("读取角度失败");
  read_datebuffer[20] = {0};
  delay(10);
  return 0;
  
  //打印测试
  //  for(int i =0; i<=9 ;i++){
  //     Serial.print(read_datebuffer[i]);
  // }
  //  Serial.println(" ");
}

void stop(int ID) {
  // stop the motor
  // ID: the id of the motor; for now there is motor 1 and motor 2
  senddate[0] = 0x3E;
  senddate[1] = 0x81; // Code 5
  senddate[2] = ID;
  senddate[3] = 0x00;
  senddate[4] = senddate[0] + senddate[1] + senddate[2] + senddate[3];
  Serial2.write(senddate,5);
}

void angle_increase_send(int ID,int32_t i_angle)
{
  senddate[0]=0x3E;
  senddate[1]=0xA7;
  senddate[2]=ID;//电机ID
  senddate[3]=0x04;
  senddate[4]=senddate[0]+senddate[1]+senddate[2]+senddate[3];
  
  senddate[5] = (uint8_t)(i_angle & 0xFF);//数据低八位
  senddate[6] = (uint8_t)((i_angle >> 8) & 0xFF);//数据高八位
  senddate[7] = (uint8_t)((i_angle >> 16) & 0xFF);//数据高八位
  senddate[8] = (uint8_t)((i_angle >> 24) & 0xFF);//数据高八位
  senddate[9]=senddate[5]+senddate[6]+senddate[7]+senddate[8];
  Serial2.write(senddate,10);
}
