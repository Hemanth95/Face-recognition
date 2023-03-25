import smbus
from time import sleep
address = 0x68
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def ini():
    bus.write_byte_data(address,SMPLRT_DIV,7)
    bus.write_byte_data(address,PWR_MGMT_1,1)
    bus.write_byte_data(address,CONFIG,0)
    bus.write_byte_data(address,GYRO_CONFIG,24)
    bus.write_byte_data(address,INT_ENABLE,1)
def read(regaddr):
     high = bus.read_byte_data(address,regaddr)
     low = bus.read_byte_data(address,regaddr+1)

     value = (high << 8) | low

     if(value>32768):
         value = value-65536
     return value



bus = smbus.SMBus(1)
ini()
while(True):
    Ax = read(ACCEL_XOUT_H)
    Ay = read(ACCEL_YOUT_H)
    Az = read(ACCEL_ZOUT_H)
    Gx =read(GYRO_XOUT_H)
    Gy =read(GYRO_YOUT_H)
    Gz =read(GYRO_ZOUT_H)
    #Ax = Ax/16384.0;
    #Ay = Ay/16384.0;
    #Az = Az/16384.0;
    #Gx = Gx/131;
    #Gy = Gy/131;
    #Gz = Gz/131;
    print((Ax,Ay,Az),(Gx,Gy,Gz))
    sleep(.5)
