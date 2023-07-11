import numpy as np
import glm
import pygame as pg

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()

    def render(self):
        self.vao.render()

    def destroy(self):
        #There is no garbage collection in OpenGL, so we need to manually delete the objects we created
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        #Vertex Array Object
        #We associated our vertex buffer with the shader program
        #we specific buffer formate ('3f') and the name of the attribute in the shader program ('in_position')
        #This is saying that in the buffer, each vertex is assigned 3 float numbers (x,y,z), and these numbers are associated with the attribute 'in_position' in the shader program
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao

    def get_vertex_data(self):
        #you can use np.float32 as f4 instead of np.float32.
        vertex_data = np.array([(-0.6, -0.8, 00), (0.6, -0.8, 0), (0, 0.8, 0)], dtype = 'f4')
        return vertex_data
    
    def get_vbo(self):
        #Need to send data to GPU as a buffer
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def get_shader_program(self, shader_name):

        """
        vertex_shader_path = f'shaders/{shader_name}.vert'
        fragment_shader_path = f'shaders/{shader_name}.frag'
        print("Vertex Shader Path: ", vertex_shader_path)
        print("Fragment Shader Path: ", fragment_shader_path)
        """

        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

class Cube:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()

        #Load texture
        self.texture = self.get_texture('textures/img_2.png')

        self.on_init()

    def get_texture(self, texture_path):

        #Since in pygame the y axis is flipped, we need to flip the image
        texture = pg.image.load(texture_path).convert()

        #First x, then y. X = false, Y = true
        texture = pg.transform.flip(texture, False, True)
        #Temporary text for lighting, fill shape with color
        texture.fill('red')
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture
    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time * 0.5, glm.vec3(0, 1, 0))
        self.shader_program['m_model'].write(m_model)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['camPos'].write(self.app.camera.position)

    def get_model_matrix(self):
        #Model Matrix
        #This is the matrix that will be used to transform the vertices of the cube
        #We will use this matrix to transform the vertices of the cube
        m_model = glm.mat4()
        return m_model
    def on_init(self):
    #Pass the projection matrix from the camera to the shader program

        self.shader_program['light.position'].write(self.app.light.position)
        self.shader_program['light.Ia'].write(self.app.light.Ia)
        self.shader_program['light.Id'].write(self.app.light.Id)
        self.shader_program['light.Is'].write(self.app.light.Is)

        #Name of texture variable in shader program and call use() on the texture
        self.shader_program['u_texture_0'] = 0
        self.texture.use()

        #mvp = m_proj * m_view * m_model method
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)
    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        # There is no garbage collection in OpenGL, so we need to manually delete the objects we created
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self):
        # Vertex Array Object
        # We associated our vertex buffer with the shader program
        # we specific buffer formate ('3f') and the name of the attribute in the shader program ('in_position')
        # This is saying that in the buffer, each vertex is assigned 3 float numbers (x,y,z), and these numbers are associated with the attribute 'in_position' in the shader program
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '2f 3f 3f', 'in_texcoord_0', 'in_normal', 'in_position')])
        return vao

    def get_vertex_data(self):
        #Vertices of a cube based on the center point at 0,0,0
        vertices = [(-1, -1, 1), (1,-1, 1), (1, 1, 1), (-1, 1, 1),
                   (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        #Triangles that make up the cube
        #By default, in OpenGL, triangles are drawn counter-clockwise
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]
        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        #normals
        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6]

        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

    #For convience, we will use a static method to get the data from the vertices and indices lists
    #Questions, what is a static method? Why do we need it?
    #Answer: a static method is a method that can be called without instantiating a class first
    #In this case, we don't need to create an instance of the Cube class to call this method
    #We can just call it directly from the class (????????)
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vbo(self):
        # Need to send data to GPU as a buffer
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def get_shader_program(self, shader_name):
        """
        vertex_shader_path = f'shaders/{shader_name}.vert'
        fragment_shader_path = f'shaders/{shader_name}.frag'
        print("Vertex Shader Path: ", vertex_shader_path)
        print("Fragment Shader Path: ", fragment_shader_path)
        """
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program