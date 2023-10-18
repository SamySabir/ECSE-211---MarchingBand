import brickpi3
import time

class Drum:
    
    def __init__(self, BP,port, rotation_angle, motor_speed=300,invert_rotation=False, starting_position="up",delay=1):
        
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
        MOTOR=None
        if (port == "A"):
            MOTOR = BP.PORT_A
        elif (port == "B"):
            MOTOR = BP.PORT_B
        elif (port == "C"):
            MOTOR = BP.PORT_C
        elif (port == "D"):
            MOTOR = BP.PORT_D
            
        self.motor=MOTOR
        
            
        #Set the motor parameters
        BP.offset_motor_encoder(self.motor, BP.get_motor_encoder(self.motor))
        BP.set_motor_limits(self.motor, self.power_limit, self.speed_limit)
        BP.set_motor_power(self.motor, 0)
        
        BP.reset_all()
        time.sleep(self.delay)
        
    def stop(self):
        self.is_stopped=True
    
    def start(self):
        self.is_stopped=False
    
    def move(self,BP):

        BP.set_motor_limits(self.motor, self.power_limit, self.motor_speed)
        print("position: ", self.position)
        #move up or move down depending on position
        if self.position == "up":
            print("in down")
            BP.set_motor_position_relative(self.motor, self.rotation_angle)
            self.position="down"  
            
        elif self.position == "down":
            print("in down")
            BP.set_motor_position_relative(self.motor, -self.rotation_angle)
            self.position="up"
            
        time.sleep(self.delay)
        BP.reset_all()
        time.sleep(self.delay)           
  
  
def main():
    print("main")
    BP = brickpi3.BrickPi3()
    drum = Drum(BP,"A", 15, starting_position="down",motor_speed=720,delay=0.1)
    
    while(1):
        drum.move(BP)
        drum.move(BP)
 
        
if __name__ == "__main__":
    main()
    
