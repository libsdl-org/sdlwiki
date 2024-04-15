###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetNumTouchFingers

Get the number of active fingers for a given touch device.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_GetNumTouchFingers(SDL_TouchID touchID);

```

## Function Parameters

|                 |                          |
| --------------- | ------------------------ |
| **touchID**     | the ID of a touch device |

## Return Value

Returns the number of active fingers for a given touch device on success or
a negative error code on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetTouchFinger](SDL_GetTouchFinger)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


