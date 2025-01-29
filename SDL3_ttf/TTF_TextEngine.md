###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_TextEngine

A text engine used to create text objects.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef struct TTF_TextEngine TTF_TextEngine;
```

## Remarks

This is a public interface that can be used by applications and libraries
to perform customize rendering with text objects. See
<SDL3_ttf/SDL_textengine.h> for details.

There are three text engines provided with the library:

- Drawing to an SDL_Surface, created with
  [TTF_CreateSurfaceTextEngine](TTF_CreateSurfaceTextEngine)()
- Drawing with an SDL 2D renderer, created with
  [TTF_CreateRendererTextEngine](TTF_CreateRendererTextEngine)()
- Drawing with the SDL GPU API, created with
  [TTF_CreateGPUTextEngine](TTF_CreateGPUTextEngine)()

## Version

This struct is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLTTF](CategorySDLTTF)

