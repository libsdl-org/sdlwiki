###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMouseInstanceName

Get the name of a mouse.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
const char* SDL_GetMouseInstanceName(SDL_MouseID instance_id);

```

## Function Parameters

|                     |                       |
| ------------------- | --------------------- |
| **instance_id**     | the mouse instance ID |

## Return Value

Returns the name of the selected mouse, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function returns "" if the mouse doesn't have a name.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetMice](SDL_GetMice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

