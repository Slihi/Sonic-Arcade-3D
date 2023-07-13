import numpy as np
import glm
import pygame as pg


class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        self.app = app

        self.pos = pos
        self.rot = glm.vec3([glm.radians(angle) for angle in rot])
        self.scale = scale

        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def get_texture(self, texture_path):

        #Since in pygame the y axis is flipped, we need to flip the image
        texture = pg.image.load(texture_path).convert()

        #First x, then y. X = false, Y = true
        texture = pg.transform.flip(texture, False, True)
        #Temporary text for lighting, fill shape with color
        #texture.fill('red')
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    #def update(self): ...

    def get_model_matrix(self):
        #Model Matrix
        #This is the matrix that will be used to transform the vertices of the cube
        #We will use this matrix to transform the vertices of the cube
        m_model = glm.mat4()

        #Translate
        m_model = glm.translate(m_model, self.pos)

        #Rotate x
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        #Rotate y
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        #Rotate z
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))

        #Scale
        m_model = glm.scale(m_model, glm.vec3(self.scale))
        return m_model

    def render(self):
        self.update()
        self.vao.render()

class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
    #mvp = m_proj * m_view * m_model method
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
    #Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Tree(BaseModel):
    def __init__(self, app, vao_name='tree', tex_id=3, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp = m_proj * m_view * m_model method
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)