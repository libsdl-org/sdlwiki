###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GL_GetCurrentContext

Get the currently active OpenGL context.

## Syntax

```c
SDL_GLContext SDL_GL_GetCurrentContext(void);

```

## Return Value

Returns the currently active OpenGL context or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GL_MakeCurrent](SDL_GL_MakeCurrent.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
