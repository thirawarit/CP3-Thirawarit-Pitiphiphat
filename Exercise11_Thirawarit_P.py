num = int(input())
#text = ''
for i in range(num) :
    text = ''
    text += ' '*(num-(i+1))     # Num -x    ลดลงไปทีละ i ในแต่ละบรรทัด i
    text += '*'*(2*i+1)         # 2x+1      เพิ่มเป็นจำนวนเลขคี่ : 1,3,5,7,9
    print(text)