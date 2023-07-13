import pygame as pg
import moderngl as glm
import pywavefront as pwf

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        #load textures from dictionary
        self.textures = {}
        self.textures[0] = self.get_texture('textures/img.png')
        self.textures[1] = self.get_texture('textures/img_1.png')
        self.textures[2] = self.get_texture('textures/img_2.png')

        #fill brown
        #Color brown
        brown = (0.5, 0.4, 0.3)
        self.textures[3] = self.solid_color_texture((0.5, 0.4, 0.3))

        """
        Parsingm involves extracting information about the materials and their associated textures 
        """

    def get_texture(self, texture_path):
        texture = pg.image.load(texture_path).convert()
        texture = pg.transform.flip(texture, False, True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        #mipmaps (To make further away textures look better)
        texture.filter = (glm.LINEAR_MIPMAP_LINEAR, glm.LINEAR)
        texture.build_mipmaps()
        # AF
        #eliminates aliasing artifacts on various textures and reduces shimmering
        texture.anisotropy = 32.0

        return texture

    def solid_color_texture(self, color):
        texture = pg.Surface((1, 1))
        texture.fill(color)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [texture.release() for texture in self.textures.values()]