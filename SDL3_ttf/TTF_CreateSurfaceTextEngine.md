###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateSurfaceTextEngine

Create a text engine for drawing text on SDL surfaces.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateSurfaceTextEngine(void);
```

## Return Value

([TTF_TextEngine](TTF_TextEngine) *) Returns a
[TTF_TextEngine](TTF_TextEngine) object or NULL on failure; call
SDL_GetError() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_DestroySurfaceTextEngine](TTF_DestroySurfaceTextEngine)
- [TTF_DrawSurfaceText](TTF_DrawSurfaceText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

