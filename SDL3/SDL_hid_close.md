###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_close

Close a HID device.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_hid_close(SDL_hid_device *dev);

```

## Function Parameters

|             |                                                               |
| ----------- | ------------------------------------------------------------- |
| **dev**     | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

