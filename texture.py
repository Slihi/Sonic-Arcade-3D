import pygame as pg
import glm

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        #load textures from dictionary
        self.textures = {}
        self.textures[0] = self.get_texture('textures/img.png')
        self.textures[1] = self.get_texture('textures/img_1.png')
        self.textures[2] = self.get_texture('textures/img_2.png')

    def get_texture(self, texture_path):
        texture = pg.image.load(texture_path).convert()
        texture = pg.transform.flip(texture, False, True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture
    def destroy(self):
        [texture.release() for texture in self.textures.values()]