###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetGrabbedWindow

Get the window that currently has an input grab enabled.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_Window* SDL_GetGrabbedWindow(void);

```

## Return Value

Returns the window if input is grabbed or NULL otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


