/**
 * @file UartDataRx.hpp
 * @author your name (you@domain.com)
 * @brief
 * @version 0.1
 * @date 2023-11-07
 *
 * @copyright Copyright (c) 2023
 *
 */

#ifndef _UARTDATARX_HPP_
#define _UARTDATARX_HPP_

#include "Arduino.h"

/*
    数据传输格式 10.5,123.5,123.5/
    中间用“,”隔开，最后以“/”结束
    */

/**
 * @brief
 *
 */
class UartDataRx
{
private:
    Stream *debugger;
    String Temp;

public:
    float data[10]; // 接收的数据,最多10个数据
    uint16_t count; // 接收到的数据个数
    String packet;
    /**
     * @brief Construct a new Uart Data Rx object
     *
     * @param s
     */
    UartDataRx(Stream &s);
    void getdata();
    void decode();
    ~UartDataRx();
};
/**
 * @brief
 *
 */
void UartDataRx::getdata()
{
    count = 0;
    if (debugger->available())
    {
        delay(1);
        packet = "";
        while (debugger->available())
        {
            packet += char(debugger->read());
        }
        decode();
    }
}
void UartDataRx::decode()
{
    if (packet.length() > 0)
    { // packet为接收到的含有数字的字符串
        count = 0;
        for (int i = 0; i < packet.length(); i++)
        {
            if (packet[i] == ',')
            {                                 // 空格为两个数值之间的隔开符号，可以是其他字符。
                data[count] = Temp.toFloat(); // toInt()为转换为整形
                Temp = "";                    // 清空，准备接收下一个数据
                count++;
            }
            else if (packet[i] == '/')
            {                                 // 结束符号    输入格式为   200 10 10 1.5/
                data[count] = Temp.toFloat(); // toFloat  转换为浮点数
                Temp = "";
                count++;
            }
            else
            {
                Temp += packet[i];
            }
        }
        packet = ""; //
    }
}
UartDataRx::UartDataRx(Stream &s)
{
    Temp = "";
    packet = "";
    count = 0;
    debugger = &s;
}

UartDataRx::~UartDataRx()
{
}
#endif // !_UARTDATARX_HPP
