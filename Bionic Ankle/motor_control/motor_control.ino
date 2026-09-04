#include <SoftwareSerial.h>


// 定义 SoftwareSerial 对象，分别指定 RX 和 TX 引脚
SoftwareSerial mySerial(10, 11); // RX, TX

//定义一个都是八位数据类型的数组  用来存放数据
uint8_t senddate[30]={};
uint8_t motor_data[10] = {};

//摇杆
const int xPin = A0;
const int yPin = A1;
const int btPin = 4;
// (x, y) to get the pos
// (0, 0) top left
// (1024, 1024) bottom right)
int x = 0;
int y = 0;
int before_x = -1;
int before_y = -1;
int dir_x = 0;
int dir_y = 0;


const int delay_constant = 100;

void setup() {
  pinMode(btPin, INPUT);
  digitalWrite(btPin, HIGH);
  // Serial.begin(115200); //初始化硬件串口
  Serial.begin(9600);
  mySerial.begin(115200);//初始化软件串口
  stop(1);
  
  while (before_x == -1) {
    before_x = (double)read_angle(1) / 100;
  }
  while (before_y == -1) {
    before_y = (double)read_angle(2) / 100;
  }
  
  

}

void loop() {
  // put your main code here, to run repeatedly:
  

  // 摇控干
  /*
  x = analogRead(xPin);
  y = analogRead(yPin);
  
  
  int angle_x = map(x, 0, 1024, 0, 359);
  int angle_y = map(y, 0, 1024, 0, 359);


  bool no_turn_x = false;
  if (angle_x == before_x) {
    no_turn_x = true;
    dir_x = 1;
  }
  else if (angle_x > before_x) {
    dir_x = 0;
  }
  else {
    dir_x = 1;
  }

  bool no_turn_y = false;
  if (angle_y == before_y) {
    no_turn_y = true;
    dir_y = 1;
  }
  else if (angle_y > before_y) {
    dir_y = 0;
  }
  else {
    dir_y = 1;
  }
  
  before_x = angle_x;
  before_y = angle_y;

  if (not no_turn_x) {
    send(1, (int64_t)angle_x * 100, dir_x);
    delay(delay_constant);
  }
  
  if (not no_turn_y) {
    send(2, (int64_t)angle_y * 100, dir_y);
    delay(delay_constant);
  }
  */

  send(1, 18000, 1);
  send(2, 18000, 1);



  delay(delay_constant);
  Serial.print("motor 1 ");
  Serial.println((double)read_angle(1) / 100);
  delay(delay_constant);
  Serial.print("motor 2 ");
  Serial.println((double)read_angle(2) / 100);
  delay(delay_constant);


}

void send(int ID,int64_t angle, bool dir) {
  // control motor rotation
  // ID: the id of the motor; for now there is motor 1 and motor 2
  // Angle: 0° - 359.99° the int64_t is from 0 - 35999
  // Direction: 0 clockwise, 1 counterclockwise

  senddate[0] = 0x3E; 
  senddate[1] = 0xA5; // Code 13
  senddate[2] = ID; //电机ID
  senddate[3] = 0x04;
  senddate[4] = senddate[0] + senddate[1] + senddate[2] + senddate[3];
  
  senddate[5] = dir;//转动方向  0顺 1逆
  senddate[6] = (uint8_t)(angle & 0xFF);//数据低八位
  senddate[7] = (uint8_t)((angle >> 8) & 0xFF);//数据高八位
  senddate[8] = 0x00; 
  senddate[9] = senddate[5] + senddate[6] + senddate[7] + senddate[8];
  mySerial.write(senddate,10);
}

void stop(int ID) {
  // stop the motor
  // ID: the id of the motor; for now there is motor 1 and motor 2
  senddate[0] = 0x3E;
  senddate[1] = 0x81; // Code 5
  senddate[2] = ID;
  senddate[3] = 0x00;
  senddate[4] = senddate[0] + senddate[1] + senddate[2] + senddate[3];
  mySerial.write(senddate,5);
}

long long int read_angle(int ID) {
  // read the angle the motor is now
  // ID: the id of the motor; for now there is motor 1 and motor 2

  // send request to motor {ID}
  senddate[0] = 0x3E;
  senddate[1] = 0x94; // Code 21
  senddate[2] = ID;
  senddate[3] = 0x00;
  senddate[4] = senddate[0] + senddate[1] + senddate[2] + senddate[3];
  mySerial.write(senddate,5);

  
  // Read in data from motor
  if (mySerial.available() >= sizeof(motor_data)) {
    mySerial.readBytes((uint8_t *)&motor_data, sizeof(motor_data));  // 读取数据到接收数据缓冲区中
  }
  /*
  for (int i = 0; i < 10; i++) {
    mySerial.println(motor_data[i]);
  }
  mySerial.println();
  */
  // find the start of the program, and get the angle 
  for (int i = 0; i < 10; i++) {
    if (motor_data[i] == 0x3E) {
      if (motor_data[(i + 1) % 10] + motor_data[(i + 2) % 10] + motor_data[(i + 3) % 10] + motor_data[(i) % 10] == motor_data[(i + 4) % 10]) {
        uint32_t angle = 0;
        angle = (uint32_t)motor_data[(i + 5) % 10] | ((uint32_t)motor_data[(i + 6) % 10] << 8) | ((uint32_t)motor_data[(i + 7) % 10] << 16) | ((uint32_t)motor_data[(i + 8) % 10] << 24);
        return (long long int)angle;
      }
    }
  }
  
  // If there is no angle, then print fail
  Serial.println("fail");
  return -1;
}



