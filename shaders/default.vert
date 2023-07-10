#version 330 core

#The OpenGL Shading Language (GLSL) is a C-style language

#
layout (location = 0) in vec3 in_position;

void main(){
    gl_Position = vec4(in_position, 1.0)
}