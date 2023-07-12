#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

// declare the light
uniform Light light;
// declare the texture
uniform sampler2D u_texture_0;
// declare the camera position
uniform vec3 camPos;

vec3 getLight(vec3 color){
    vec3 Normal = normalize(normal);
    // ambient light
    //Multiply the color of the object by the ambient light

    vec3 ambient = light.Ia;
    // diffuse light
    //Multiply the color of the object by the diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(dot(Normal, lightDir), 0.0);
    vec3 diffuse = diff * light.Id;

    // specular light
    //Multiply the color of the object by the specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    // pow(x, y) = x^y
    // 32 is intensity of the specular light
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    return color * (ambient + diffuse + specular);
}

void main(){
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = getLight(color);
    fragColor = vec4(color, 1.0);

}