from model import *

class Scene:
    def __init__(self,app):
        self.app = app
        self.objects = []
        self.load()

    def add_objects(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_objects


        '''
        If you use high detail textures far away, it will look very grainy
        If you use low detail textures close up, it will look very blurry
        OpenGL has a solution for this called mipmaps
        Mipmaps are a set of textures with different resolutions
        The texture with the highest resolution is the first mipmap
        The texture with the lowest resolution is the last mipmap
        '''
        n, s = 80, 2

        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, s, z)))

        add(Tree(app, pos=(0, 0, 10)))

    def render(self):
        for obj in self.objects:
            obj.render()
