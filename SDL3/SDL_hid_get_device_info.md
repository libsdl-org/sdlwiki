# SDL_hid_get_device_info

Get the device info from a HID device.

## Header File

Defined in [<SDL3/SDL_hidapi.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
SDL_hid_device_info * SDL_hid_get_device_info(SDL_hid_device *dev);
```

## Function Parameters

|                                    |         |                                                               |
| ---------------------------------- | ------- | ------------------------------------------------------------- |
| [SDL_hid_device](SDL_hid_device) * | **dev** | a device handle returned from [SDL_hid_open](SDL_hid_open)(). |

## Return Value

([SDL_hid_device_info](SDL_hid_device_info) *) Returns a pointer to the
[SDL_hid_device_info](SDL_hid_device_info) for this hid_device or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information. This
struct is valid until the device is closed with
[SDL_hid_close](SDL_hid_close)().

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

