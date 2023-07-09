import arcade
import random


# Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"
perspective_point = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]

#Key List
keys = []

# Window Class
class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        arcade.set_background_color(arcade.color.AMAZON)
        
        #Set Minimum Screen Size
        Minimum_Screen_Width = 800
        Minimum_Screen_Height = 600
        self.set_minimum_size(Minimum_Screen_Width, Minimum_Screen_Height)




    def setup(self):
        pass

    def on_key_press(self, key, modifiers):
        keys.append(key)


    def on_key_release(self, key, modifiers):
        keys.remove(key)

    
    def on_draw(self):
        arcade.start_render()

        perspective_dot = arcade.draw_circle_filled(perspective_point[0], perspective_point[1], 5, arcade.color.BLACK)



    def on_update(self, delta_time):
        pass

#Objects


if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()








