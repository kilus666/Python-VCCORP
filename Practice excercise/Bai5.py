import pickle
import turtle
import time


a=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] 

# Khởi tạo class point bao gồm tọa độ x, y
# value cho biết point là đường hay tường hay điểm đến (đường là 0, tường là 1, điểm đến là 2) 
# flag cho biết một điểm đã đi qua hay chưa
# parent cho biết điểm trước đó phục vụ cho việc vẽ lại đường dẫn sau này
# distance cho biết khoảng cách chim bay từ điểm đến đích

class point:
    
    def __init__(self,x,y,value=None):
        self.x=x
        self.y=y
        self.value=value
        self.flag= None
        self.parent= None
        self.g=0
        self.distance= None
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.__hash__()== other.__hash__()

# method cho tính khoảng cách cho mỗi điểm
    def setDistance(self):
        self.distance= ((self.x-end.x)**2+(self.y-end.y)**2)**(1/2) + self.g

# Lưu thông tin các điểm trên ma trận vào một danh sách
ListofPoint=[]
for y, hang in enumerate(a):
    for x, value in enumerate(hang):
            A= point(x,20-y,value)
            ListofPoint.append(A)

# Đặt end point, start point
# openList chứa các điểm là điểm đi có thể đi được(không phải tường) và chưa đi qua
# openList được sắp xếp sao cho điểm có khoảng cách đã đi cộng khoảng cách tới đích là nhỏ nhất luôn nằm đầu danh sách
# path là list chứa các điểm tạo nên đường


openList=[]
path=[]
openList=[]
closedList=[]
count=0
# Tạo hàm giải mê cung

def solve(startPoint):
    global count
    global openList
    global closedList
    startPoint.setDistance()
    # Thêm điểm start vào trong openList
    openList.append(startPoint)

    while len(openList)>0:
        # Tạo bộ đếm đế tính số lần chạy vòng lặp để tìm ra tổng số bước phải chạy nhằm tìm ra đường tối ưu
        count+=1
        # cho điểm hiện tại là điểm nằm đầu danh sách openList ( điểm này luôn thỏa mãn có khoảng cách đã đi và khoảng cách đến đích ngắn nhất)
        curr= openList[0]
        # Cho điểm hiện tại vào closeList nhằm đánh dấu điểm đã đi qua
        closedList.append(curr)

        # Kiểm tra điểm hiện tại xem nó có phải đích không, nếu có thì dừng lại và tạo nên path, hiện thị số bước, và thông tin điểm đã dc tìm thấy
        if curr.value==2:
            path.append({curr.x: curr.y})
            print("Number of steps: ", count)
            while curr.parent != None:
                path.append({curr.parent.x: curr.parent.y})
                curr= curr.parent
            break
        # Tạo danh sách tạm những điểm là hàng xóm của điểm hiện tại, danh sách bao gồm các điểm chưa đi qua và k phải tường
        neighbors=[]
        for key, value in enumerate(ListofPoint):
            if value== curr:
                if curr.x==0:
                    for i in [1,-31,31]:
                        neighbor= ListofPoint[key+i]
                        if neighbor in closedList or neighbor.value==1:
                            pass
                        else:
                            neighbor.parent= curr # thêm điểm hiện tại là cha của các điểm hàng xóm, phục vụ cho việc tạo path
                            neighbor.g= curr.g+1 # Tính toán số bước đã đi để đến được điểm hàng xóm này
                            neighbor.setDistance() # tính bộ khoảng cách
                            neighbors.append(neighbor) # Thêm điểm này vào danh sách các điểm hàng xóm
                else:
                    for i in [-1,1,-31,31]:
                        neighbor= ListofPoint[key+i]
                        if neighbor in closedList or neighbor.value==1:
                            pass
                        else:
                            neighbor.parent= curr
                            neighbor.g= curr.g+1
                            neighbor.setDistance()
                            neighbors.append(neighbor)
        # kiểm tra trong danh sách điểm hàng xóm mới tạo, có điểm nào
        # đã tồn tại trong openList hay chưa, nếu có, kiểm tra điểm trong openList đã có số bước đã đi tối ưu hay chưa
        # Nếu chưa cần phải thay đổi điểm đang có trong openList, và xóa điểm ở trong danh sách điểm hàng xóm
        # Nếu rồi chỉ cần xóa điểm này khỏi dánh sách điểm hàng xóm để k tạo thêm duplicate trong openList
        
        for index, value in enumerate(openList):
                for j,i in enumerate(neighbors):
                    if value==i:
                        if value.g> i.g:
                            openList[index]= i
                            del neighbors[j]
                        else:
                            del neighbors[j]
        
        
        # Thêm tất cả các điểm còn lại trong danh sách hàng xóm vào cuối danh sách openList
        for i in neighbors:
            openList.append(i)
        # Xóa điểm ở đầu danh sách openList, cũng chính là điểm hiện tại lúc này
        del openList[0]
        # Sắp xếp lại openList để điểm đứng đầu là tối ưu
        for i in range(0,len(openList)):
            if openList[0].distance> openList[i].distance:
                openList[0], openList[i]= openList[i], openList[0]
    
    if len(openList)==0:
        print("Cannot find the path")

end= point(11,5)
start= point(0,10)
timeStart= time.time()
print(" ")
print("Start")
print(" ")
solve(start)
print(" ")
print("Finish")
print(" ")
timeStop= time.time()
duration = timeStop-timeStart
print("Total finding time: ", round(duration,2))
print(" ")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
turtle.ht()
def writing_text(string, position=[0,0], color="white", font_size=30, font_type='bold'):
    turtle.color(color)
    turtle.goto(position)
    turtle.write(string, align= "Center", font=("Arial", font_size, font_type))

def startProtocol():
    turtle.color("white")
    turtle.write("3", align= "Center", font=("Arial", 30, "bold"))
    time.sleep(1)
    turtle.clear()

    turtle.color("white")
    turtle.write("2", align= "Center", font=("Arial", 30, "bold"))
    time.sleep(1)
    turtle.clear()

    turtle.color("white")
    turtle.write("1", align= "Center", font=("Arial", 30, "bold"))
    time.sleep(1)
    turtle.clear()

    turtle.color("white")
    turtle.write("Start", align= "Center", font=("Arial", 30, "bold"))
    turtle.up()
    time.sleep(1)
    turtle.clear()
def set_up_background():
    wn= turtle.Screen()
    wn.bgcolor("black")
    wn.title("A Maze game")
    wn.setup(700,700)
def drawing():
    pen= Pen()
    for y, day in enumerate(a):
        for x, val in enumerate(day):
            
                realX= -300+x*20
                realY= -200+(20-y)*20

                if val==1:
                    pen.goto(realX,realY)
                    pen.stamp()
                elif val==2:
                    pen.color("red")
                    pen.goto(realX,realY)
                    pen.stamp()
                    pen.color("white")

    turtle.penup()
    for i in range(len(path)-1,0,-1):
        for x,y in path[i].items():
            
            turtle.speed(0)
            turtle.pensize(6)
            turtle.pen(pencolor= "blue")
            turtle.setposition(-300+ x*20,-200+y*20)
            turtle.pendown()

set_up_background()
startProtocol()
drawing()

turtle.penup()

writing_text("Finish")
time.sleep(0.5)

writing_text(string= "Total run time: "+ str(round(duration,2)), position=[0,-30], font_size=12, font_type='italic')
turtle.getscreen()._root.mainloop()
