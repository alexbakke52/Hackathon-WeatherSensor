#include <Dps3xx.h>

Dps3xx Dps3xxPressureSensor = Dps3xx();

void setup() 
{
  Serial.begin(9600);
  Dps3xxPressureSensor.begin(Wire);
}

void loop() 
{
  // put your main code here, to run repeatedly:

}
