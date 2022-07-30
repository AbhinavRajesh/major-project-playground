#ifndef UTILS_H
#define UTILS_H

#include<cmath>
#include<tuple>
#include<vector>

float distance(float p1[3], float p2[3]) {
    float x = pow(p1[0] - p2[0], 2);
    float y = pow(p1[1] - p2[1], 2);
    float z = pow(p1[2] - p2[2], 2);

    return sqrt(x + y + z);
}

std::tuple<float, float, float> get_angles(float p1[3], float p2[3]) {
    float a = p1[0] - p2[0];
    float b = p1[1] - p2[1];
    float c = p1[2] - p2[2];

    float l = sqrt(a*a + b*b + c*c);

    float x = acos(a/l);
    float y = acos(b/l);
    float z = acos(c/l);

    return  { x, y, z };
}

std::vector<std::vector<float>> get_euler_rot_matrix(float x, float y, float z) {
    float cx = cos(x);
    float cy = cos(y);
    float cz = cos(z);

    float sx = sin(x);
    float sy = sin(y);
    float sz = sin(z);

    std::vector<std::vector<float>> euler_rot_matrix = {
      { cy * cz, (sx * sy * cz) - (cx * sz), (cx * sy * sz) - (sx * cz), 0 },
      { cy * sz, (sx * sy * sz) - (cx * cz), (cx * sy * sz) - (sx * cz), 0 },
      { -sy, sx * cy, cx * cy, 0 },
      { 0, 0, 0, 1 }
    };

    return euler_rot_matrix;
}

template <typename T>
std::vector<std::vector<T>> get_translation_matrix(T tx, T ty, T tz) {
    return {
        { 1, 0, 0, tx},
        { 0, 1, 0, ty},
        { 0, 0, 1, tz},
        { 0, 0, 0, 1},
    };
}

template <typename T>
std::vector<std::vector<T>> get_scale_matrix(T sx, T sy, T sz) {
    return {
        { sx, 0, 0, 0},
        { 0, sy, 0, 0},
        { 0, 0, sz, 0},
        { 0, 0, 0, 1},
    };
}

std::vector<std::vector<float>> get_x_rotation_matrix(float theta) {
    float cos_t = cos(theta);
    float sin_t = sin(theta);
    
    return {
        { 1, 0, 0, 0 },
        { 0, cos_t, -sin_t, 0 },
        { 0, sin_t, cos_t, 0 },
        { 0, 0, 0, 1 }
    };
}

std::vector<std::vector<float>> get_y_rotation_matrix(float theta) {
    float cos_t = cos(theta);
    float sin_t = sin(theta);
    
    return {
        { cos_t, 0, -sin_t, 0 },
        { 0, 1, 0, 0 },
        { sin_t, 0, cos_t, 0 },
        { 0, 0, 0, 1 }
    };
}

std::vector<std::vector<float>> get_z_rotation_matrix(float theta) {
    float cos_t = cos(theta);
    float sin_t = sin(theta);
    
    return {
        { cos_t, -sin_t, 0, 0 },
        { sin_t, cos_t, 0, 0 },
        { 0, 0, 1, 0 },
        { 0, 0, 0, 1 }
    };
}

#endif 