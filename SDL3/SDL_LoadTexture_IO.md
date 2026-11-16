# SDL_LoadTexture_IO

Load a BMP, PNG or JPEG image from a seekable SDL data stream.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Texture * SDL_LoadTexture_IO(SDL_Renderer *renderer, SDL_IOStream *src, bool closeio);
```

## Function Parameters

|                                |              |                                                                                                      |
| ------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer** | the renderer to use.                                                                                 |
| [SDL_IOStream](SDL_IOStream) * | **src**      | the data stream for the texture.                                                                     |
| bool                           | **closeio**  | if true, calls [SDL_CloseIO](SDL_CloseIO)() on `src` before returning, even in the case of an error. |

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
- [SDL_LoadTexture](SDL_LoadTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

