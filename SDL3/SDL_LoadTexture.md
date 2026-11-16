# SDL_LoadTexture

Load a BMP, PNG or JPEG image from a file.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Texture * SDL_LoadTexture(SDL_Renderer *renderer, const char *file);
```

## Function Parameters

|                                |              |                      |
| ------------------------------ | ------------ | -------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer to use. |
| const char *                   | **file**     | the file to load.    |

## Return Value

([SDL_Texture](SDL_Texture) *) Returns a pointer to a new
[SDL_Texture](SDL_Texture) structure or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The new texture should be freed with
[SDL_DestroyTexture](SDL_DestroyTexture)(). Not doing so will result in a
memory leak.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_DestroyTexture](SDL_DestroyTexture)
- [SDL_LoadTexture_IO](SDL_LoadTexture_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

