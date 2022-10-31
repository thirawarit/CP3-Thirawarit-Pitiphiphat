'''
====MAIN====
Project : ลิฟต์คอนโด 2 ตัว
-เริ่มต้นที่ชั้น 1 ทั้ง 2 ตัว
-หากลิฟต์อยู่ชั้นเดียวกันจะเรียก ลิฟต์ตัวที่ 1 เสมอ
-หากเรียกลิฟต์ที่อยู่ต่างชั้นกัน จะเรียกลิฟต์ที่อยู่ใกล้กับชั้นนั้นที่สุด

-รับค่า ชั้นที่เรียก และ ชั้นที่จะไป
input = integer: 0 > N > 20 or code service : 505
input = 
    1.integer: ตั้งค่าจำนวนชั้นของคอนโด
    2.integer: เรียกลิฟต์ที่ใกล้ชั้นนั้นที่สุด หากอยู่ชั้นเดียวกันให้ลิฟต์1ไปรับเสมอ
    3.integer: รับเลขชั้นที่ต้องการจะไป
**** หากต้องการหยุดloop ให้ใส่อักษร 505 ลงใน input
'''
import time


class Setup_Lift:
    #1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th 11st
    ordinal_floor = []
    def __init__(self) -> None:
        pass
    def cal_ordinal(self, num_floor: int):
        self.num_floor = num_floor
        for i in range(self.num_floor):
            if 0 < (i+1)%10 <= 3:
                self.ordinal_floor.append(str(i+1) + ['st', 'nd', 'rd'][i%10])
            else:
                self.ordinal_floor.append(str(i+1) + 'th')
    

class Lift_Work(Setup_Lift):
    call_lift = int()
    position_lift = 1
    lift_terminal = int()
    ordinal_floor = Setup_Lift.ordinal_floor
    def get_passenger(self, call_lift: int):
        self.call_lift = call_lift
        print("Lift's coming...")
        time.sleep(2)
        print(self.ordinal_floor[self.call_lift-1],", Lift's opening...")
        self.position_lift = self.call_lift
    def lift_move(self, lift_terminal: int):
        self.lift_terminal = lift_terminal
        if self.lift_terminal < self.position_lift:
            self.position_lift = self.lift_terminal
            print("Lift's going down...")
            time.sleep(2)
            print(self.ordinal_floor[self.lift_terminal-1])
        elif self.lift_terminal > self.position_lift:
            self.position_lift = self.lift_terminal
            print("Lift's going up...")
            time.sleep(2)
            print( self.ordinal_floor[self.lift_terminal-1])
        else:
            print("lift's opening...")
            time.sleep(0.5)
            print(self.ordinal_floor[self.lift_terminal-1])
    def check_status(self, num_lift):
        if num_lift == 1:
            print("========","\nLift1 is",self.position_lift)
        else:
            print("Lift2 is",self.position_lift,"\n"+"========")


code_service = 505
setup_numfloor = Setup_Lift()
setup_numfloor.cal_ordinal(int(input("Set lifts in the building >> :")))
print(setup_numfloor.ordinal_floor)
lift1 = Lift_Work()
lift2 = Lift_Work()

lift1.check_status(1)
lift2.check_status(2)
while True:
    try:
        call = int(input('call lift from floor : '))
    except ValueError:
        print("************", 
              "ERROR System input wrong data!!!", 
              "Only interger such as : 0, 12, 345", 
              "************", 
              sep='\n'
              )
        break
    if call == code_service:
        print("Manual mode - SERVICE")
        break
    elif abs(lift1.position_lift-call) <= abs(lift2.position_lift-call):
        lift1.get_passenger(call)
        lift_terminal = int(input('Select Floor that you want : '))
        lift1.lift_move(lift_terminal)
    elif abs(lift1.position_lift-call) > abs(lift2.position_lift-call):
        lift2.get_passenger(call)
        lift_terminal = int(input('Select Floor that you want : '))
        lift2.lift_move(lift_terminal)
    lift1.check_status(1)
    lift2.check_status(2)

