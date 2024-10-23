###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetTouchFingers

Get a list of active fingers for a given touch device.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
SDL_Finger ** SDL_GetTouchFingers(SDL_TouchID touchID, int *count);
```

## Function Parameters

|                            |             |                                                                       |
| -------------------------- | ----------- | --------------------------------------------------------------------- |
| [SDL_TouchID](SDL_TouchID) | **touchID** | the ID of a touch device.                                             |
| int *                      | **count**   | a pointer filled in with the number of fingers returned, can be NULL. |

## Return Value

([SDL_Finger](SDL_Finger) **) Returns a NULL terminated array of
[SDL_Finger](SDL_Finger) pointers or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This is a single
allocation that should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

