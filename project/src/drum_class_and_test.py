from utils.brick import Motor, BP
import time



class Drum:
    
    def __init__(self,port, rotation_angle, motor_speed=300,invert_rotation=False, starting_position="up",delay=1):
        
        self.is_stopped     = True
        self.delay          = delay
        
        self.power_limit    = 80
        self.speed_limit    = 720
        self.motor_speed    = motor_speed
    
        self.rotation_angle = rotation_angle
        if (invert_rotation):
            self.rotation_angle = -self.rotation_angle
        
        self.position       = starting_position
        
        
        #Associate motor to the brick pi port

        self.motor=Motor(port)
        
            
        #Set the motor parameters
        self.motor.offset_encoder(self.motor.get_encoder())
        self.motor.set_limits(self.power_limit, self.speed_limit)
        self.motor.set_power(0)
        
        #self.motor.reset_position()
        #self.motor.reset_encoder()
        #BP.reset_all()
        time.sleep(self.delay)
        
    def stop(self):
        self.is_stopped=True
    
    def start(self):
        self.is_stopped=False
    
    def move(self):

        self.motor.set_limits(self.power_limit, self.motor_speed)
        print("position: ", self.position)
        #move up or move down depending on position
        if self.position == "up":
            print("in down")
            self.motor.set_position_relative(self.rotation_angle)
            self.position="down"  
            
        elif self.position == "down":
            print("in down")
            self.motor.set_position_relative(-self.rotation_angle)
            self.position="up"
            
        time.sleep(self.delay)
        #self.motor.reset_position()
        #self.motor.reset_encoder()
        #BP.reset_all()
        time.sleep(self.delay)           
  

def drummer(event, activated):
    print("start drummer")
 
    drum = Drum("A", 15, starting_position="down",motor_speed=720,delay=0.1)
    
    event.wait()
    try:
        
        while True:
            print(3)
            drum.move()
            drum.move()
        
    except BaseException as e:
        BP.reset_all()
        print(e)
        exit()
        
        




def main():
    print("main")
   
    drum = Drum("A", 15, starting_position="down",motor_speed=720,delay=0.12)
    
    while(1):
        drum.move()
        drum.move()
 
        
if __name__ == "__main__":
    main()
    
