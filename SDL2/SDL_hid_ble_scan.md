###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_ble_scan

Start or stop a BLE scan on iOS and tvOS to pair Steam Controllers 

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
void SDL_hid_ble_scan(SDL_bool active);

```

## Function Parameters

|                |                                                                                 |
| -------------- | ------------------------------------------------------------------------------- |
| **active**     | [SDL_TRUE](SDL_TRUE) to start the scan, [SDL_FALSE](SDL_FALSE) to stop the scan |

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


