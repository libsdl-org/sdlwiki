###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CreateGLTextEngine

Create a text engine for drawing text with OpenGL.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_TextEngine * TTF_CreateGLTextEngine(void);
```

## Return Value

([TTF_TextEngine](TTF_TextEngine) *) Returns a
[TTF_TextEngine](TTF_TextEngine) object or NULL on failure; call
SDL_GetError() for more information.

## Remarks

The caller is responsible for ensuring the correct OpenGL context is
current when calling this function and when using the resulting text
engine.

The GL text engine and all text created with it become invalid if the
OpenGL context is destroyed. Destroy the engine before destroying the
context.

## Thread Safety

This function should be called on the thread that created the OpenGL
context.

## Version

This function is available since SDL_ttf 3.3.0.

## See Also

- [TTF_CreateGLTextEngineWithProperties](TTF_CreateGLTextEngineWithProperties)
- [TTF_DestroyGLTextEngine](TTF_DestroyGLTextEngine)
- [TTF_GetGLTextDrawData](TTF_GetGLTextDrawData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

