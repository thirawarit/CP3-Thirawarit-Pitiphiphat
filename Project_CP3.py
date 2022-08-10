'''
Project : ลิฟต์คอนโด 2 ห้อง
-เริ่มต้นที่ชั้น 1 ทั้ง 2 อัน
-รับค่า ห้องในชั้นนั้น โดยมีรายละเอียดคือ เลขที่ดิน/(ชั้น,เลขลำดับห้อง) เช่น 66/956
-เมื่อส่งลูกบ้านแล้ว ให้ลิฟต์ที่ใกล้ชั้นที่ลูกบ้านที่2 ไปรับลูกบ้าน ลงมา
'''
class Lift_Work:
    call_lift = int()
    lift = int()
    lift_terminal = int()
    order_floor = ['st', 'nd', 'ed', 'th', 'th', 'th', 'th', 'th']
    def lift_move(self)
        if self.lift_terminal < self.lift:
            self.lift = self.lift_terminal
            print("lift's going down...", self.lift_terminal, order_floor[self.lift_terminal-1])
        elif self.lift_terminal > self.lift:
            self.lift = self.lift_terminal
            print("lift's going up...", self.lift_terminal, order_floor[self.lift_terminal-1])
        else:
            print("lift's opening...", self.lift_terminal, order_floor[self.lift_terminal-1])



lift1 = 1
lift2 = 1
order_floor = ['st', 'nd', 'ed', 'th', 'th', 'th', 'th', 'th']
lift1_go = int(input("lift1's opening... , Select Floor that you want : "))
lift1 = lift1_go
print("lift's going up...", lift1_go, order_floor[lift1_go-1])
print("========","\nlift1 is",lift1)
print("lift2 is",lift2)
while True:
    personcalls = int(input('call lift from floor : '))
    if abs(lift1-personcalls) <= abs(lift2-personcalls):
        lift1 = personcalls
        print(personcalls, order_floor[personcalls-1], 'lift1 open!!')
        lift1_go = int(input('Select Floor that you want : '))
        if lift1_go < lift1:
            lift1 = lift1_go
            print("lift's going down...", lift1_go, order_floor[lift1_go-1])
        elif lift1_go > lift1:
            lift1 = lift1_go
            print("lift's going up...", lift1_go, order_floor[lift1_go-1])
        else:
            print("lift's opening...", lift1_go, order_floor[lift1_go-1])
    elif abs(lift1-personcalls) > abs(lift2-personcalls):
        lift2 = personcalls
        print(personcalls, order_floor[personcalls-1], 'lift2 open!!')
        lift2_go = int(input('Select Floor that you want : '))
        if lift2_go < lift2:
            lift2 = lift2_go
            print("lift's going down...", lift2_go, order_floor[lift2_go-1])
        elif lift2_go > lift2:
            lift2 = lift1_go
            print("lift's going up...", lift2_go, order_floor[lift2_go-1])
        else:
            print("lift's opening...", lift2_go, order_floor[lift2_go-1])
    '''
    else:
        print("lift1's coming...")
        lift1_go = int(input("lift's opening... , Select Floor that you want : "))
        lift1 = lift1_go
        print("lift's going up...", lift1_go, order_floor[lift1_go-1])
        '''
    print("========","\nlift1 is",lift1)
    print("lift2 is",lift2)
