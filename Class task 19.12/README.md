# Class task 

## 19.12.18

*cinema task
```cmd
py 00_task.py
```

class CinemaRoom:
    def __init__(self,MyMovie):
        self.chairMatrix=[[False for i in range(10)] for j in range(8)]
        self.MyMovie=MyMovie
    def BuyChairs(self,amount):
        for row in range(len(self.chairMatrix)):
            for col in range (len(self.chairMatrix[row])):
                if not self.chairMatrix[row][col]:
                    amount-=1
                    self.chairMatrix[row][col]=True
                if amount==0:
                    break
            if amount==0:
                break
        return amount==0
    def GetDescription(self):
        res=""
        res+="Movie in this room {}".format(self.MyMovie.GetDescription())
        res += "\n\nThe ChairMatrix in the room (V= orderded, X = not ordered)\n"
        for row in self.chairMatrix:
            for col in row:
                if col:
                    res+=" V | " 
                else:
                    res+=" X | "
            res += "\n------------------------------------------------\n"
        return res

class Cinema:
    def __init__(self):
        self.movies_arr = [None for i in range(100)]
        self.rooms_arr = [None for i in range(6)]
    def BuyTicket(self,movieName,amount):
        res=False
        for i in range (len(self.rooms_arr)):
            if self.rooms_arr[i] != None and self.rooms_arr[i].MyMovie.movie_name==movieName:
                res=self.rooms_arr[i].BuyChairs(amount)
        return res
    def GetDescription(self):
        str1=""
        for i in range(len(self.rooms_arr)):
            if self.rooms_arr[i] != None:
                str1+="\n--------------------Room number{}---------------------\n".format(i+1)
                str1+= self.rooms_arr[i].GetDescription()
        return str1
 
class Movie:
    def __init__(self,length,movie_name):
        self.length=length
        self.movie_name=movie_name 
    def GetDescription(self):
        return "Movie name {} length of the movie {}".format(self.movie_name,self.length)

m1=movie(90,"avatar")
m2=movie(75,"avengers")

room1=CinemaRoom(m1)
room2=CinemaRoom(m2)

myCinema=cinema()

myCinema.rooms_arr[0]=room1
myCinema.rooms_arr[1]=room2

myCinema.BuyTicket("avatar", 4)
myCinema.BuyTicket("avengers", 6)

print(myCinema.GetDescription())


*output

--------------------Room number1---------------------
Movie in this room Movie name avatar length of the movie 90

The ChairMatrix in the room (V= orderded, X = not ordered)
 V |  V |  V |  V |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------

--------------------Room number2---------------------
Movie in this room Movie name avengers length of the movie 75

The ChairMatrix in the room (V= orderded, X = not ordered)
 V |  V |  V |  V |  V |  V |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------
 X |  X |  X |  X |  X |  X |  X |  X |  X |  X |
------------------------------------------------

