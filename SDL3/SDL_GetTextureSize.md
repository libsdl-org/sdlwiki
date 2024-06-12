###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTextureSize

Get the size of a texture, as floating point values.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_GetTextureSize(SDL_Texture *texture, float *w, float *h);
```

## Function Parameters

|                              |             |                                                                                                                             |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query                                                                                                        |
| float *                      | **w**       | a pointer filled in with the width of the texture in pixels. This argument can be NULL if you don't need this information.  |
| float *                      | **h**       | a pointer filled in with the height of the texture in pixels. This argument can be NULL if you don't need this information. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

