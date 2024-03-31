###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTouchDeviceName

Get the touch device name as reported from the driver.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
const char* SDL_GetTouchDeviceName(SDL_TouchID touchID);

```

## Function Parameters

|                 |                               |
| --------------- | ----------------------------- |
| **touchID**     | the touch device instance ID. |

## Return Value

Returns touch device name, or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

You do not own the returned string, do not modify or free it.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

