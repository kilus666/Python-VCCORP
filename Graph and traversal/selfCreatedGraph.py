openList= []
closeList=[]

class point:
    def __init__(self, name, x, y):
        self.name= name
        self.horizontal= x
        self.vertical= y
        self.g=None
        self.f= None
        self.parrent= None
        

# Graph Class
class graph:
    V={}
    edges= {}

    #insert Point function
    def insertPoint(self, value):
        if isinstance(value, point) and value not in self.V:
            self.V[value.name]=  value
            self.edges[value.name]= {}
        else:
            print("ERROR POINT ")

    # insert Edges function
    def insertEdges(self, point1, point2):
        if point1 in self.V and point2 in self.V:
            distance= abs(((self.V[point1].horizontal- self.V[point2].horizontal)^2+(self.V[point1].vertical- self.V[point2].vertical)**2)**(1/2))
            self.edges[point1][point2]= distance
            self.edges[point2][point1]= distance
        else:
            print("Error")

    # print Graph
    def printGraph(self):
        for v, i in sorted(self.edges.items()):
            print(v + " : "+ str(i))

    # A* find path

    def findPath(self, start, ending):
        # set startPoint and endPoint and add startPoint to the openList
        
        startPoint= point(start,self.V[start].horizontal,self.V[start].vertical)
        endPoint= point(ending,self.V[ending].horizontal,self.V[ending].vertical)
        startPoint.g= 0
        startPoint.f= startPoint.g+ abs(((startPoint.horizontal- endPoint.horizontal)**2+(startPoint.vertical- endPoint.vertical)**2)**(1/2))
        openList.append(startPoint)
        # as long as openList have value in it, continue to run
        while len(openList)>0:
            # find the point with the largest f
            
            curr= openList[0]
            currIndex = 0
            for index, item in enumerate(openList):
                if item.f < curr.f:
                    curr = item
                    currIndex = index
            
            #set current node equals to openList with least f value, remove current node from the openList and put it in closeList
            
            del openList[0]
            closeList.append(curr.name)

            # if the current Node is goal, end the function
            if curr.name== endPoint.name:
                path=[]
                while curr!=None:
                    path.append(curr.name)
                    curr= curr.parrent
                return print(path[::-1])

           
            # check current Node neighbor through the edges list(edge list have have the form: nameNode: [{its neighbor name: distance}]
            # iterate over the list of neighbors of current node and create children
            children=[]
            for key, value in self.edges[curr.name].items():
                child= point(key, self.V[key].horizontal, self.V[key].vertical)
                child.parrent= curr
                children.append(child)
  
                for closedChild in closeList:
                    if child.name== closedChild:
                        continue
             
                child.g= curr.g+ self.edges[child.name][child.parrent.name]
                child.f= child.g+ abs(((child.horizontal- endPoint.horizontal)**2+(child.vertical- endPoint.vertical)**2)**(1/2))
                
                for open_node in openList:
                    if child == open_node and child.g > open_node.g:
                        continue

            # Add the child to the open list
                openList.append(child)



Graph= graph()
A= point("A", 1, 3)
B= point("B", 2, 3)
C= point("C", 2, 1)
D= point("D", 1, 1)
E= point("E", 3, 1)
F= point("F", 3, 0)
G= point("G", 3, 3)
H= point("H", 2, 0)
K= point("K", 3, 0)
list1= [A,B,C,D,E,F,G,H,K]
for i in list1:
    Graph.insertPoint(i)


listEdges= ["AB","AD","BG","BD","BC", "CD", "CH", "CE", "EK", "EG", "GF",'DF',"AF"]
for i in listEdges:
    Graph.insertEdges(i[0], i[1])


Graph.findPath("A","F")



