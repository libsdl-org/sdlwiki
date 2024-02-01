###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetRenderDrawColorspace

Set the colorspace used for drawing operations 

## Syntax

```c
int SDL_SetRenderDrawColorspace(SDL_Renderer *renderer, SDL_Colorspace colorspace);

```

## Function Parameters

|                    |                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------ |
| **renderer**       | the rendering context                                                                      |
| **colorspace**     | an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace for drawing operations |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The default colorspace for drawing operations is
[SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB), but you can change it to other
colorspaces such as [SDL_COLORSPACE_SCRGB](SDL_COLORSPACE_SCRGB) for HDR
rendering.

This does not affect the colorspace of textures, which is specified via
properties when the texture is created and does not change.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderDrawColorspace](SDL_GetRenderDrawColorspace)

----
[CategoryAPI](CategoryAPI)

