import pygame as pg
import moderngl as glm

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
        #mipmaps (To make further away textures look better)
        texture.filter = (glm.LINEAR_MIPMAP_LINEAR, glm.LINEAR)
        texture.build_mipmaps()
        # AF
        #eliminates aliasing artifacts on various textures and reduces shimmering
        texture.anisotropy = 32.0

        return texture
    def destroy(self):
        [texture.release() for texture in self.textures.values()]