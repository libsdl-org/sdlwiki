###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderDrawColorspace

Get the colorspace used for drawing operations 

## Syntax

```c
int SDL_GetRenderDrawColorspace(SDL_Renderer *renderer, SDL_Colorspace *colorspace);

```

## Function Parameters

|                    |                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **renderer**       | the rendering context                                                                                               |
| **colorspace**     | a pointer filled in with an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace for drawing operations |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderDrawColorspace](SDL_SetRenderDrawColorspace)

----
[CategoryAPI](CategoryAPI)

