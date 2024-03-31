###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_WarpMouseGlobal

Move the mouse to the given position in global screen space.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_WarpMouseGlobal(float x, float y);

```

## Function Parameters

|           |                  |
| --------- | ---------------- |
| **x**     | the x coordinate |
| **y**     | the y coordinate |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function generates a mouse motion event.

A failure of this function usually means that it is unsupported by a
platform.

Note that this function will appear to succeed, but not actually move the
mouse when used over Microsoft Remote Desktop.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_WarpMouseInWindow](SDL_WarpMouseInWindow)

----
[CategoryAPI](CategoryAPI), [CategoryMouse](CategoryMouse), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


