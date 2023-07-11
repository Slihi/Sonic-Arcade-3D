import glm
# PyGLM is a wrapper for the C++ library GLM (OpenGL Mathematics)

#Camera Parameters
FOV = 50 #Degrees
NEAR = 0.1
FAR = 100

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WINDOW_SIZE[0] / app.WINDOW_SIZE[1]
        #Position of the camera in the up direction
        self.position = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)

        #view matrix
        self.m_view = self.get_view_matrix()

        #Porjection Matrix
        self.m_proj = self.get_projection_matrix()

    def get_view_matrix(self):
    #Eye ''position of camera'', Center ''position where the camera is looking at, 'up' normalized up vector, how the camera is oriented
        return glm.lookAt(self.position, glm.vec3(0), self.up)
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)