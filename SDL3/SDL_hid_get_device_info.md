###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_get_device_info

Get the device info from a HID device.

## Syntax

```c
SDL_hid_device_info * SDL_hid_get_device_info(SDL_hid_device *dev);

```

## Function Parameters

|             |                                                               |
| ----------- | ------------------------------------------------------------- |
| **dev**     | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |

## Return Value

Returns a pointer to the [SDL_hid_device_info](SDL_hid_device_info) for
this hid_device, or NULL in the case of failure; call
[SDL_GetError](SDL_GetError)() for more information. This struct is valid
until the device is closed with [SDL_hid_close](SDL_hid_close)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

