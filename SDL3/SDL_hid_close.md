# SDL_hid_close

Close a HID device.

## Header File

Defined in [<SDL3/SDL_hidapi.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
int SDL_hid_close(SDL_hid_device *dev);
```

## Function Parameters

|                                    |         |                                                               |
| ---------------------------------- | ------- | ------------------------------------------------------------- |
| [SDL_hid_device](SDL_hid_device) * | **dev** | a device handle returned from [SDL_hid_open](SDL_hid_open)(). |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

