# """ BÀI 8. Cho hai lớp Country và City có các thuộc tính (như bên dưới). Một quốc gia có 1 thủ đô và có thể
# có 1 hoặc nhiều thành phố. Một thành phố luôn trực thuộc chỉ 1 quốc gia.
# - Country:
# + String code (mã quốc gia)
# + String name
# + String continent (mã lục địa)
# + double surfaceArea (diện tích bề mặt)
# + int population (dân số)
# + double gnp (Gross National Product)
# + int capital (mã thành phố là thủ đô của đất nước này)- City:
# + int id
# + String name
# + int population (dân số của thành phố)
# - Dữ liệu về các quốc gia, thành phố được lưu trong 2 file countries.dat và cities. Hãy thực hiện đọc thông
# tin các thành quốc, quốc gia từ file
# sau đó sử dụng lambda và stream api trong java 8 để thực hiện các yêu cầu sau:
# 1.1 Tìm thành phố đông dân nhất của mỗi quốc gia.
# 1.2 Tìm thành phố đông dân nhất của mỗi lục địa.
# 1.3 Tìm thành phố là thủ đô, đông dân nhất.
# 1.4 Tìm thành phố là thủ đô, đông dân nhất của mỗi lục địa.
# 1.5 Sắp xếp các quốc gia theo số lượng thành phố giảm dần.
# 1.6 Sắp xếp các quốc gia theo mật độ dân số theo thứ tự giảm dần bỏ qua các quốc gia có dân số bằng
# không """

# import os
# import csv
# import re
# import pandas as pd
# import pickle
# import sqlite3

# listFile= []
# currentPath= os.getcwd()
# path= os.path.join(currentPath,"input_8")
# for root, dirs, files in os.walk(path):
#     for file in files:
#         filePath= os.path.join(root, file)
#         listFile.append(filePath)

# cities= pd.DataFrame()


# # cities.set_index()

# # read cities.dat to a list of lists
# ID= []
# Name=[]
# Population=[]
# Code=[]

# datContent = [i.strip().split() for i in open(f"{listFile[0]}").readlines()]

# for city in datContent:

#         i= re.split("=|,|]",city[1])
#         ID.append(int(i[1]))
#         n= " ".join(city[2:-2])
#         n= re.split("=|,|]",n)[1]
#         Name.append(n)
#         p= re.split("=|,|]",city[-2])
#         Population.append(int(p[1]))
#         c= re.split("=|,|]",city[-1])
#         Code.append(c[1])

# cities.insert(0,"ID",ID,False)
# cities.insert(1,"Name",Name,False)
# cities.insert(2,"Population",Population,False)
# cities.insert(3,"CountryCode",Code,False)
# cities.set_index("ID",inplace=True)






# countries= pd.DataFrame()
# Code=[]
# Name=[]
# Continent=[]
# surfaceArea=[]
# Population=[]
# gnp=[]
# capital=[]

# datContent = [i.strip().split() for i in open(f"{listFile[1]}").readlines()]

# for country in datContent:

#         c= re.split("=|,|}",country[0])
#         Code.append(c[1])
#         nco= " ".join(country[1:-4])
#         B= re.split("=",nco)
#         n= B[1].split(",")[0]
#         con=B[-1].split(",")[0]
#         Name.append(n)
#         Continent.append(con)
#         s= re.split("=|,|]",country[-4])
#         surfaceArea.append(s[1])
#         p= re.split("=|,|]",country[-3])
#         Population.append(int(p[1]))
#         g= re.split("=|,|]",country[-2])
#         gnp.append(int(p[1]))
#         c= re.split("=|,|]|}",country[-1])
#         capital.append(int(c[1]))


# countries.insert(0,"Code",Code,False)
# countries.insert(1,"Name",Name,False)
# countries.insert(2,"Continent",Continent,False)
# countries.insert(3,"surfaceArea",surfaceArea,False)
# countries.insert(4,"Population",Population,False)
# countries.insert(5,"gnp",gnp,False)
# countries.insert(6,"Capital",capital,False)
# countries.set_index("Code",inplace=True)
# countries.to_csv("Countries.csv")

# conn= sqlite3.connect("Data.db")
# countries.to_sql("Countries", conn)
# cities.to_sql("Cities", conn)

import sqlite3
conn= sqlite3.connect("Data.db")
c= conn.cursor()
with conn:

# Cau 1

        c.execute("""Select C.Name, city.Name, Max(city.Population) as Population
                From Countries as C 
                Left Join Cities as city 
                ON C.Code= city.CountryCode
                Group by C.name

                """)
        p=c.fetchall()
        for i in p:
                print(i)
        print(" ")
# Cau 2
        c.execute("""Select C.Continent, city.Name, Max(city.Population) as Population
                From Countries as C 
                Left Join Cities as city 
                ON C.Code= city.CountryCode
                Group by C.Continent

                """)
        p=c.fetchall()
        for i in p:
                print(i)
        print(" ")

# Cau 3
        c.execute("""Select C.Capital, city.Name, Max(city.Population) as Population
                From Countries as C 
                Left Join Cities as city 
                ON C.Capital= city.ID
                """)
        p=c.fetchall()
        for i in p:
                print(i)
        print(" ")

# Cau 4
        c.execute("""Select C.Continent, C.Capital, city.Name, Max(city.Population) as Population
                From Countries as C 
                Left Join Cities as city 
                ON C.Capital= city.ID
                Group by C.Continent
                """)
        p=c.fetchall()
        for i in p:
                print(i)
        print(" ")

# Cau 5
        c.execute("""Select C.Name, city.Name, Count(*) as Number
                From Countries as C 
                Left Join Cities as city 
                ON C.Code= city.CountryCode
                Group by C.Name
                Order by Number DESC

                """)
        p=c.fetchall()
        for i in p:
                print(i)
        print(" ")

# Cau 6


        conn.commit()
        c.execute("Select Name, Population, PPA From Countries Where Population<>0 Order By PPA DESC")
        a=c.fetchall()
        for i in a:
                print(i)
















