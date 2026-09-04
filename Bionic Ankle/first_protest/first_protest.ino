#include <SoftwareSerial.h>

// 定义 SoftwareSerial 对象，分别指定 RX 和 TX 引脚
SoftwareSerial mySerial(10, 11);  // RX, TX

//定义一个都是八位数据类型的数组  用来存放数据
uint8_t senddate[30] = { 0 };
uint8_t read_datebuffer[20] = { 0 };
uint32_t receivedData;
float read_angle;
//摇杆
const int xPin = A0;
const int yPin = A1;
const int btPin = 4;

//电机数据  1电机中值 138.43  抬脚尖 减小 最值 5   底脚尖  增大  最值 185
//电机数据  2电机中值 234.63  抬脚尖 减小 最值 60  底脚尖  增大  最值 340
int x = 0;
int y = 0;
float angle1 = 0.0;
float angle2 = 0.0;
bool direction1;
bool direction2;
float targetangle1 = 138.43;
float targetangle2 = 234.63;

void setup() {
  pinMode(btPin, INPUT);
  digitalWrite(btPin, HIGH);
  Serial.begin(115200);    //初始化硬件串口
  mySerial.begin(115200);  //初始化软件串口
}

void loop() {
  // put your main code here, to run repeatedly:
  x = analogRead(xPin);
  y = analogRead(yPin);
  angle1 = map(x, 0, 1024, 5, 185);
  angle2 = map(y, 0, 1024, 60, 340);
  if (targetangle1 > angle1) {
    direction1 = 1;
    send(1, int64_t(angle1 * 100), direction1);
  } else if (targetangle1 < angle1) {
    direction1 = 0;
    send(1,int64_t(angle1*100),direction1);
  }
  if (targetangle2 > angle2) direction2 = 1;
  else if (targetangle2 < angle2) direction2 = 0;
  targetangle1 = angle1;
  targetangle2 = angle2;
  Serial.print("angle1:");
  Serial.print(angle1);
  Serial.print(direction1);
  Serial.print("  angle2:");
  Serial.print(angle2);
  Serial.println(direction2);


  send(2, int64_t(angle2 * 100), direction2);
  delay(50);
}

//定义一个打印数组的函数用来查看数组数据
void printArray(const uint8_t *array, size_t length) {
  for (size_t i = 0; i < length; i++) {
    Serial.print(array[i], HEX);  // 以十六进制格式打印每个元素
    Serial.print(" ");
  }
  Serial.println();  // 换行
}

//定义发送转动角度函数
/*单圈位置闭环控制命令 1
主机发送该命令以控制电机的位置（单圈角度）。
1. 控制值 spinDirection 设置电机转动的方向，为 uint8_t 类型，0x00 代表顺时针，0x01 代表
逆时针
2. 控制值 angleControl 为 uint16_t 类型，数值范围 0~35999，对应实际位置为 0.01degree/LSB，
即实际角度范围 0°~359.99°。
帧命令（5byte，含校验）
CMD[0] 帧头 0x3E
CMD[1] 命令 0xA5
CMD[2] ID 0x01~0x20
CMD[3] 数据长度 0x04
CMD_SUM 帧命令校验和字节 CMD[0]~CMD[3]字节校验和
帧数据（5byte，含校验）
DATA[0] 转动方向字节 DATA[0] = spinDirection
DATA[1] 位置控制字节 1 DATA[1] = *(uint8_t *)(&angleControl)
DATA[2] 位置控制字节 2 DATA[2] = *((uint8_t *)(&angleControl)+1)
DATA[3] NULL 0x00
DATA_SUM 数据校验字节 DATA[0]~DATA[3]字节校验和
备注：
1. 该命令下电机的最大速度由上位机中的 Max Speed 值限制。
2. 该控制模式下，电机的最大加速度由上位机中的 Max Acceleration 值限制。
3. 该控制模式下，MF、MH、MG 电机的最大转矩电流由上位机中的 Max Torque Current
值限制；MS 电机的最大功率由上位机中的 Max Power 值限制。
*/

void send(int ID, int64_t angle, bool dir) {
  senddate[0] = 0x3E;
  senddate[1] = 0xA5;
  senddate[2] = ID;  //电机ID
  senddate[3] = 0x04;
  senddate[4] = senddate[0] + senddate[1] + senddate[2] + senddate[3];

  senddate[5] = dir;                             //转动方向  0顺 1逆
  senddate[6] = (uint8_t)(angle & 0xFF);         //数据低八位
  senddate[7] = (uint8_t)((angle >> 8) & 0xFF);  //数据高八位
  senddate[8] = 0x00;
  senddate[9] = senddate[5] + senddate[6] + senddate[7] + senddate[8];
  mySerial.write(senddate, 10);
}
float single_read(int ID)  //电机单圈角度读取
{
  uint8_t readdate[5] = { 0 };
  uint8_t temp = 0;
  readdate[0] = 0x3E;
  readdate[1] = 0x94;
  readdate[2] = ID;
  readdate[3] = 0x00;
  readdate[4] = readdate[0] + readdate[1] + readdate[2] + readdate[3];
  mySerial.write(readdate, 5);
  //数据接收
  if (mySerial.available() >= sizeof(read_datebuffer)) {
    mySerial.readBytes((uint8_t *)&read_datebuffer, sizeof(read_datebuffer));  // 读取数据到接收数据缓冲区中
  }
  for (int i = 0; i < 11; i++) {
    if (read_datebuffer[i] == 0x3E) {
      temp = read_datebuffer[i] + read_datebuffer[i + 1] + read_datebuffer[i + 2] + read_datebuffer[i + 3];
      if (read_datebuffer[i + 4] == temp) {
        receivedData = (uint32_t)read_datebuffer[i + 5] | ((uint32_t)read_datebuffer[i + 6] << 8) | ((uint32_t)read_datebuffer[i + 7] << 16) | ((uint32_t)read_datebuffer[i + 8] << 24);
        float readangle = (float)receivedData / 100.00;
        return readangle;
      }
    }
  }
  Serial.println("读取角度失败");
  return 0;
  //打印测试
  //  for(int i =0; i<=9 ;i++){
  //     Serial.print(read_datebuffer[i]);
  // }
  //  Serial.println(" ");
}
