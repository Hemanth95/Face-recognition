import socket
import RPi.GPIO as gpio
host=''
port=5560
print(gpio.RPI_INFO)
gpio.setmode(gpio.BOARD)
pin = 12
gpio.setup(pin,gpio.OUT,initial=0)  
pwm = gpio.PWM(pin,440)

def socketsetup():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)
    print("socket binding complete")
    return s
def setupconnection():
    s.listen(1)
    conn,addr = s.accept()
    print("connected to "+addr[0]+":"+ str(addr[1]))
    return conn
def getdata(conn):
    data=conn.recv(1024)
    data=data.decode('utf-8')
    return data
def understand_data(conn):
    height = 0;
    while True:
        fb=0;
        lr=0;
        data = getdata(conn)
        if data == 'exit':
            
            print('client just left')
            conn.close()
            break
        if data =='kill':
            print(' ops socket closed')
            s.close()
            break
        while data == 'moving up':
            height = height+1;
            print(height)
            #pwm.start(height)
            data = getdata(conn)
                
        while data == 'moving down':
            height = height-1;
            print(height)
           # pwm.start(height)
            data = getdata(conn)
                
                
        while data == 'front':
            fb = fb+1;
            print(fb)
            
            
            
            data= getdata(conn)
                
                
        while data == 'back':
            fb = fb-1;
            print(fb)
            data= getdata(conn)
            
        if data =='right':
            print(data)
            
        if data == 'left':
            print(data)
            
            
    return;
        

s = socketsetup()
while True:
    
    try:
        conn = setupconnection()
        print('connected')
        understand_data(conn)
      
    except:
        break

