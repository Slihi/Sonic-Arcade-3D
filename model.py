import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

    def get_vertex_data(self):
        #you can use np.float32 as f4 instead of np.float32.
        vertex_data = np.array([(-0.6, -0.8, 00), (0.6, -0.8, 0), (0, 0.8, 0)], dtype = 'np.float32')
        return vertex_data
    
    def get_vbo(self):
        #Need to send data to GPU as a buffer
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    