'''
Project : ลิฟต์คอนโด 2 ห้อง
-เริ่มต้นที่ชั้น 1 ทั้ง 2 อัน
-รับค่า ห้องในชั้นนั้น โดยมีรายละเอียดคือ เลขที่ดิน/(ชั้น,เลขลำดับห้อง) เช่น 66/956
-เมื่อส่งลูกบ้านแล้ว ให้ลิฟต์ที่ใกล้ชั้นที่ลูกบ้านที่2 ไปรับลูกบ้าน ลงมา
'''
class Lift_Work:
    call_lift = int()
    position_lift = int()
    lift_terminal = int()
    order_floor = ['st', 'nd', 'ed', 'th', 'th', 'th', 'th', 'th']
    def get_passenger(self):
        print("Lift's coming...")
        print(self.call_lift, self.order_floor[self.call_lift-1],", Lift's opening...")
    def lift_move(self):
        if self.lift_terminal < self.position_lift:
            self.position_lift = self.lift_terminal
            print("lift's going down...", self.lift_terminal, self.order_floor[self.lift_terminal-1])
        elif self.lift_terminal > self.position_lift:
            self.position_lift = self.lift_terminal
            print("lift's going up...", self.lift_terminal, self.order_floor[self.lift_terminal-1])
        else:
            print("lift's opening...", self.lift_terminal, self.order_floor[self.lift_terminal-1])
    def check_status(self, num_lift):
        if num_lift == 1:
            print("========","\nlift1 is",self.position_lift)
        else:
            print("lift2 is",self.position_lift,"\n"+"========")


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
    personcalls = int(input('call lift from floor : '))
    if abs(lift1.position_lift-personcalls) <= abs(lift2.position_lift-personcalls):
        lift1.call_lift = personcalls
        lift1.get_passenger()
        lift1.lift_terminal = int(input('Select Floor that you want : '))
        lift1.lift_move()

    elif abs(lift1.position_lift-personcalls) > abs(lift2.position_lift-personcalls):
        lift2.call_lift = personcalls
        lift2.get_passenger()
        lift2.lift_terminal = int(input('Select Floor that you want : '))
        lift2.lift_move()    
    lift1.check_status(1)
    lift2.check_status(2)
