# CSCI 596 Final Project

## Inspiration

Writing an OpenGL program to animate simulation has always been an interesting idea to me. One day I saw a beautiful picture of the sea that I took at the beach. 
![IMG_3662](https://user-images.githubusercontent.com/60117688/145937092-cff9072a-ffd3-4c00-86a0-c55835793b8d.JPG)

Then I thought it would be interesting to simulate the movement of the sea waves. And Instead of using C++ with openGL as people normally do, I decide to use Python combining openGL to implement it.
I'm also inspired by thses cool technical youtubers: https://www.youtube.com/channel/UCbqziZij4Gcow_0M5qJVW1A/videos, https://www.youtube.com/c/MarkJay/videos


## Description

While most of openGL programs are implemented with C++, I think combining openGL with another programming language would be interesting. Here I chose to simulate an animation using openGL and Python. The goal of this program is to simulate the movement of the sea waves.


## Requirement

There are several packages used in this program: PyQtGraph, opensimplex, numpy, sys. Note that PyQtGraph requires one of PyQt4, PyQt5 or PySide. One of these packages sould be imported before PyQtGraph. 


## Version

This program is based on Python 3.9.7 and PyOpenGL 3.1.1a1. Note that to make the program run properly, the version of PyOpenGL should match the version of Python.


## Implementation

I set up a window in PyOpenGL and created a 3D mesh object to represent the surface of water. After setting up the mesh object, its location and color will be changed according to time. To simulate the movement of wave, I used gradient noise function implemented in OpenSimplex. These noise were then updated to mesh object so that it could simulate animation.
More details about OpenSimplex: https://github.com/lmas/opensimplex


## Parameters

| Parameters    | Function                                 |
| ------------- |:----------------------------------------:|
| speed         | change the speed of the wave movement    |
| height        | change the height of each wave           |
| noiseType     | change the noise type that is used       |
| nsteps        | change the width of each wave            |

input the parameters from command line:
![link](https://user-images.githubusercontent.com/60117688/145937327-07adec81-5f43-412e-a0ba-d568572cff56.png)


## Display

The .mov files displaying the result of this program has been attached under the 'result' folder.

2D noise:
![](/Users/yugao/Desktop/2D.png)

3D noise:
![This is a alt text.](/image/sample.png "This is a sample image.")

4D noise:
![This is a alt text.](/image/sample.png "This is a sample image.")

## Discovery

In the process of adjusting these parameters, I found that high value of height does not reflect a good wave movement. While the moving speed is high, the differences between 2D, 3D and 4D are not obvious.




