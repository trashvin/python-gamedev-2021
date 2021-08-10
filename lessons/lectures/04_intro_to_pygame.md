# introduction to pygame

Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.

SDL or Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D.

## main advatages of pygame
- Pygame is highly portable and runs on nearly every platform and operating system.
- Pygame itself has been downloaded millions of times.
- Pygame is free. Released under the LGPL licence, you can create open source, freeware, shareware, and commercial games with it. 

## main features of pygame
- supports multi-core CPU's
- uses optimized C and Assembly codes for core functions 
- truly portable and supports many OS
- its simple
- you control your main loop
- uses small amount of code
- modular
- developers respond quickly to reported bugs.

## installation
```
pip install pygame
```
## importing ang initializing pygame

```
# for this line to work, make sure you have installed pygame

import pygame
```

```
# it is required to initialize pygame and some components needed by your program

pygame.init()

# to initialize its font componen

pygame.font.init|()
```

## moving objects

pygame uses a display __Surface__. This is basically an image that is visible on the screen, and the image is made up of pixels. 

the main way you change these pixels is by calling the __blit()__ function. This copies the pixels from one image onto another.

The basic concept of moving images:
1. copy the image to be moved
2. erase the image from the old position
3. __blit()__ the image to its new position

Note : By rapidly erasing the image and redrawing it in a new place, we achieve the "illusion" of movement.




