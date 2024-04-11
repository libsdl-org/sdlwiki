###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDLTest_SurfaceImage_s

Type for test images.

## Header File

Defined in [SDL_test_images.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_test_images.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef struct SDLTest_SurfaceImage_s {
  int width;
  int height;
  unsigned int bytes_per_pixel; /* 3:RGB, 4:RGBA */
  const char *pixel_data;
} SDLTest_SurfaceImage_t;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

