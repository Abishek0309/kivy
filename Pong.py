from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.behaviors.drag import ReferenceListProperty
from kivy.uix.accordion import NumericProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.accordion import ObjectProperty
from random import randint

class Paddle(Widget):
    score=NumericProperty(0)
    def bounce(self,ball):
        if self.collide_widget(ball):
            ball.velocity_x*=-1.1

class PongBall(Widget):
   velocity_x= NumericProperty(0)
   velocity_y= NumericProperty(0)
   velocity = ReferenceListProperty(velocity_x,velocity_y)
   
  
#Latest pos = current velocity+current pos
#this should be in vector form

   def move(self):
       self.pos=Vector(*self.velocity)+self.pos 

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 =ObjectProperty(None)
    player2 =ObjectProperty(None)
    
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self,dt):
        self.ball.move()
    #bounce from top to bottom subtract 50 to avoid the half ball to be  disappear
        if(self.ball.y<0) or (self.ball.y>self.height-50):
            self.ball.velocity_y*=-1

    #bounce from right to left subtract 50 to avoid the half ball to be  disappear
        if self.ball.x<0:
            self.ball.velocity_x*=-1
            self.player1.score+=1
        if self.ball.x>self.width-50:
            self.ball.velocity_x*=-1
            self.player2.score+=1            
        self.player1.bounce(self.ball)
        self.player2.bounce(self.ball)
    def on_touch_move(self, touch):
        if touch.x<self.width / 1/4:
            self.player1.center_y=touch.y
        if touch.x>self.width*3/4:
            self.player2.center_y=touch.y         
        
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game

if __name__ == '__main__':
    PongApp().run()