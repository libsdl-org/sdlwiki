###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT

A variable that is the address of another [SDL_Window](SDL_Window)* (as a hex string formatted with "%p").

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT    "SDL_VIDEO_WINDOW_SHARE_PIXEL_FORMAT"
```

## Remarks

If this hint is set before [SDL_CreateWindowFrom](SDL_CreateWindowFrom)()
and the [SDL_Window](SDL_Window)* it is set to has
[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL) set (and running on WGL only,
currently), then two things will occur on the newly created
[SDL_Window](SDL_Window):

1. Its pixel format will be set to the same pixel format as this
[SDL_Window](SDL_Window). This is needed for example when sharing an OpenGL
context across multiple windows.

2. The flag [SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL) will be set on the new
window so it can be used for OpenGL rendering.

This variable can be set to the following values: The address (as a string
"%p") of the [SDL_Window](SDL_Window)* that new windows created with
[SDL_CreateWindowFrom](SDL_CreateWindowFrom)() should share a pixel format
with.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)
<!-- #See the Style Guide for instructions on editing the footer. -->


