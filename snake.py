from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segnmemt(position)
            
    def add_segnmemt(self, position):
        seg = Turtle("square")
        seg.color('white')
        seg.penup()
        seg.goto(position)
        self.body.append(seg)

    def extend(self):
        self.add_segnmemt(self.body[-1].position())
        

    def move(self):
        for i in range(len(self.body)-1,0,-1):
        # snake segnments going to the next segnment coordination 3-->2 2-->1 and 1 will decide the direction to move
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
        self.body[0].fd(MOVE_DISTANCE)
    
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)