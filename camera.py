import glm
import pygame as pg
# PyGLM is a wrapper for the C++ library GLM (OpenGL Mathematics)

#Camera Parameters
FOV = 50 #Degrees
NEAR = 0.1
FAR = 100
SPEED = 0.02
SENSITIVITY = 0.05

class Camera:
    def __init__(self, app, position=(0, 0 , 4), yaw = -90, pitch = 0):
        self.app = app
        self.aspect_ratio = app.WINDOW_SIZE[0] / app.WINDOW_SIZE[1]
        #Position of the camera in the up direction
        self.position = glm.vec3(position)

        # movement vectors
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        #Euler angles
        self.yaw = yaw
        self.pitch = pitch

        #view matrix
        self.m_view = self.get_view_matrix()

        #Porjection Matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        #Limit pitch
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()

        self.m_view = self.get_view_matrix()
        self.m_proj = self.get_projection_matrix()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.position += self.forward * velocity
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.position -= self.forward * velocity
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.position -= self.right * velocity
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position -= self.up * velocity
        if keys[pg.K_e]:
            self.position += self.up * velocity


    def get_view_matrix(self):
    #Eye ''position of camera'', Center ''position where the camera is looking at, 'up' normalized up vector, how the camera is oriented
        return glm.lookAt(self.position, self.position + self.forward, self.up)
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)