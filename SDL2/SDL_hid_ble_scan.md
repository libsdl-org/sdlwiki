# SDL_hid_ble_scan

Start or stop a BLE scan on iOS and tvOS to pair Steam Controllers

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
void SDL_hid_ble_scan(SDL_bool active);
```

## Function Parameters

|                      |            |                                                                                  |
| -------------------- | ---------- | -------------------------------------------------------------------------------- |
| [SDL_bool](SDL_bool) | **active** | [SDL_TRUE](SDL_TRUE) to start the scan, [SDL_FALSE](SDL_FALSE) to stop the scan. |

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

