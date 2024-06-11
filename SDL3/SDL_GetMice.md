###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMice

Get a list of currently connected mice.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_MouseID* SDL_GetMice(int *count);
```

## Function Parameters

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| **count**     | a pointer filled in with the number of mice returned |

## Return Value

Returns a 0 terminated array of mouse instance IDs which should be freed
with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

Note that this will include any device or virtual driver that includes
mouse functionality, including some game controllers, KVM switches, etc.
You should wait for input from a device before you consider it actively in
use.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetMouseInstanceName](SDL_GetMouseInstanceName)
- [SDL_HasMouse](SDL_HasMouse)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

