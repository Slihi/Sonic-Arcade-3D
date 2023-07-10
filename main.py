import pygame as pg
import moderngl as mg
import sys

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DEEP_OCEAN_BLUE = (0.08, 0.16, 0.18)
OAK = (0.36, 0.25, 0.20)
PAPER_TOWEL_BROWN = (0.80, 0.73, 0.64)
GREEN_HILL_GREEN = (0.36, 0.80, 0.20)
SUNNY_DAY_SKY_BLUE = (0.53, 0.81, 0.98)

#Screen Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sonic Pygame 3D"


class GraphicsEngine:
    def __init__(self, width, height):
        
        pg.init()

        self.WINDOW_SIZE = (width, height)

        #Set Window Title
        pg.display.set_caption(SCREEN_TITLE)

        #Window Color
        self.WINDOW_COLOR = SUNNY_DAY_SKY_BLUE

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)


        #Create OpenGl context
        pg.display.set_mode(self.WINDOW_SIZE, flags= pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)

        #Detect and use existing OpenGl context
        self.ctx = mg.create_context()

        #Create an object to help track time
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def render(self):
        # clear frame buffer
        #* must be in front of tuple because it unpacks it into arguments for the function
        self.ctx.clear(*self.WINDOW_COLOR)
        #Swap front and back buffers
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)

if __name__ == '__main__':
    window = GraphicsEngine(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.run()



