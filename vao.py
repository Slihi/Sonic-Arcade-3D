from vbo import VBO
from shader_program import ShaderProgram

# VAO is a class that contains a VBO and a ShaderProgram object. Stands for Vertex Array Object
class VAO:
    def __init__(self,ctx):
        # CTX is the context of the OPEN GL WINDOW
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        self.vaos['cube'] = self.get_vao(self.program.programs['default'],
                                         self.vbo.vbos['cube'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attributes)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()

