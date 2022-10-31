'''
Project : ลิฟต์คอนโด 2 ตัว
-เริ่มต้นที่ชั้น 1 ทั้ง 2 ตัว
-หากลิฟต์อยู่ชั้นเดียวกันจะเรียก ลิฟต์ตัวที่ 1 เสมอ
-หากเรียกลิฟต์ที่อยู่ต่างชั้นกัน จะเรียกลิฟต์ที่อยู่ใกล้กับชั้นนั้นที่สุด

-รับค่า ชั้นที่เรียก และ ชั้นที่จะไป
-
'''
import string


class Setup_Lift:
    #1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th 11st
    ordinal_floor = []
    num_floor = int()
    def cal_ordinal(self):
        for i in range(self.num_floor):
            if 0 < (i+1)%10 <= 3:
                self.ordinal_floor.append(str(i+1) + ['st', 'nd', 'rd'][i%10])
            else:
                self.ordinal_floor.append(str(i+1) + 'th')
    

class Lift_Work(Setup_Lift):
    call_lift = int()
    position_lift = int()
    lift_terminal = int()
    ordinal_floor = Setup_Lift.ordinal_floor
    def get_passenger(self):
        print("Lift's coming...")
        print(self.call_lift, self.ordinal_floor[self.call_lift-1],", Lift's opening...")
    def lift_move(self):
        if self.lift_terminal < self.position_lift:
            self.position_lift = self.lift_terminal
            print("lift's going down...", self.lift_terminal, self.ordinal_floor[self.lift_terminal-1])
        elif self.lift_terminal > self.position_lift:
            self.position_lift = self.lift_terminal
            print("lift's going up...", self.lift_terminal, self.ordinal_floor[self.lift_terminal-1])
        else:
            print("lift's opening...", self.lift_terminal, self.ordinal_floor[self.lift_terminal-1])
    def check_status(self, num_lift):
        if num_lift == 1:
            print("========","\nlift1 is",self.position_lift)
        else:
            print("lift2 is",self.position_lift,"\n"+"========")


setup_numfloor = Setup_Lift()
setup_numfloor.num_floor = int(input("Set lifts in the building >> :"))
setup_numfloor.cal_ordinal()
print(setup_numfloor.ordinal_floor)
lift1 = Lift_Work()
lift2 = Lift_Work()
lift1.position_lift = 1
lift2.position_lift = 1
lift1_go = int(input("lift1's opening... , Select Floor that you want : "))
lift1.position_lift = lift1_go
lift1.check_status(1)
lift2.check_status(2)
'''
print("lift's going up...", lift1.position_lift, Lift_Work.order_floor[lift1_go-1])
print("========","\nlift1 is", lift1.position_lift)
print("lift2 is",lift2.position_lift)
'''
while True:
    personcalls = input('call lift from floor : ')
    if personcalls.upper() == 'STOP':
        print("************\nEmergency Stop!\n************")
        break
    elif abs(lift1.position_lift-int(personcalls)) <= abs(lift2.position_lift-int(personcalls)):
        lift1.call_lift = personcalls
        lift1.get_passenger()
        lift1.lift_terminal = int(input('Select Floor that you want : '))
        lift1.lift_move()
    elif abs(lift1.position_lift-int(personcalls)) > abs(lift2.position_lift-int(personcalls)):
        lift2.call_lift = personcalls
        lift2.get_passenger()
        lift2.lift_terminal = int(input('Select Floor that you want : '))
        lift2.lift_move()


    lift1.check_status(1)
    lift2.check_status(2)
