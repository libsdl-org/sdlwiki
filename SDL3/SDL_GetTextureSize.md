###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTextureSize

Get the size of a texture, as floating point values.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_GetTextureSize(SDL_Texture *texture, float *w, float *h);
```

## Function Parameters

|                              |             |                                                                                                                             |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Texture](SDL_Texture) * | **texture** | the texture to query.                                                                                                       |
| float *                      | **w**       | a pointer filled in with the width of the texture in pixels. This argument can be NULL if you don't need this information.  |
| float *                      | **h**       | a pointer filled in with the height of the texture in pixels. This argument can be NULL if you don't need this information. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

