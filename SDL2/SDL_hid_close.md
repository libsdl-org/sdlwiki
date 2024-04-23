###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_close

Close a HID device.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
void SDL_hid_close(SDL_hid_device *dev);

```

## Function Parameters

|             |                                                               |
| ----------- | ------------------------------------------------------------- |
| **dev**     | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

