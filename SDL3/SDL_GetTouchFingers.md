###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTouchFingers

Get a list of active fingers for a given touch device.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
extern DECLSPEC SDL_Finger **SDLCALL SDL_GetTouchFingers(SDL_TouchID touchID, int *count);

```

## Function Parameters

|                 |                                                                       |
| --------------- | --------------------------------------------------------------------- |
| **touchID**     | the ID of a touch device                                              |
| **count**       | a pointer filled in with the number of fingers returned, can be NULL. |

## Return Value

Returns a NULL terminated array of [SDL_Finger](SDL_Finger) pointers which
should be freed with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

