###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_hid_ble_scan

Start or stop a BLE scan on iOS and tvOS to pair Steam Controllers.

## Header File

Defined in [<SDL3/SDL_hidapi.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
void SDL_hid_ble_scan(bool active);
```

## Function Parameters

|      |            |                                                 |
| ---- | ---------- | ----------------------------------------------- |
| bool | **active** | true to start the scan, false to stop the scan. |

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

