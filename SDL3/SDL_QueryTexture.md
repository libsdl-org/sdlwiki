###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_QueryTexture

Query the attributes of a texture.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
int SDL_QueryTexture(SDL_Texture *texture, SDL_PixelFormatEnum *format, int *access, int *w, int *h);

```

## Function Parameters

|                 |                                                                                                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **texture**     | the texture to query                                                                                                                                                                                                                                         |
| **format**      | a pointer filled in with the raw format of the texture; the actual format may differ, but pixel transfers will use this format (one of the [SDL_PixelFormatEnum](SDL_PixelFormatEnum) values). This argument can be NULL if you don't need this information. |
| **access**      | a pointer filled in with the actual access to the texture (one of the [SDL_TextureAccess](SDL_TextureAccess) values). This argument can be NULL if you don't need this information.                                                                          |
| **w**           | a pointer filled in with the width of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                   |
| **h**           | a pointer filled in with the height of the texture in pixels. This argument can be NULL if you don't need this information.                                                                                                                                  |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_Texture* source;

// loading etc ...

int w, h;
SDL_QueryTexture(source, NULL, NULL, &w, &h);

```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)


