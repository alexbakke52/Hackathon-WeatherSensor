#include <Dps310.h>
#include <Dps368.h>
#include <Dps422.h>
#include <DpsClass.h>
#include <iostream>

Dps368 Dps368PressureSensor = Dps368();

void setup() 
{
  Serial.begin(9600);
  //Dps368PressureSensor.begin(Wire);
  Dps3xxPressureSensor.begin(SPI, pin_cs);
  Dps368PressureSensor.startMeasureTempCont(64, 64,64,64);

  std::cout<<"This somewhat works LINE 16"<<std::endl;

  uint8_t temp_mr = 2; //actual value: 2^(temp_mr)
  uint8_t temp_osr= 2; // actual value: 2^(temp_osr)
}

void loop() 
{
  uint8_t pressureCount = 20; //for example
  float pressure[pressureCount];
  uint8_t temperatureCount = 20;// for example
  float temperature[temperatureCount];

  Serial.println();
  Serial.print(temperatureCount);
  Serial.println(" temperature values found: ");
  for (int16_t i = 0; i < temperatureCount; i++)
  {
    std::cout<<temperature[i]<<std::endl;
    Serial.print(temperature[i]);
    Serial.println(" degrees of Celsius");
  }

  Serial.println();
  Serial.print(pressureCount);
  Serial.println(" pressure values found: ");
  
  for (int16_t i = 0; i < pressureCount; i++)
  {
    std::cout<<pressure[i]<<std::endl;
    Serial.print(pressure[i]);
    Serial.println(" Pascal");
  }
}
