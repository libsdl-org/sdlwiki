###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_get_report_descriptor

Get a report descriptor from a HID device.

## Syntax

```c
int SDL_hid_get_report_descriptor(SDL_hid_device *dev, unsigned char *buf, size_t buf_size);

```

## Function Parameters

|                  |                                                               |
| ---------------- | ------------------------------------------------------------- |
| **dev**          | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |
| **buf**          | The buffer to copy descriptor into.                           |
| **buf_size**     | The size of the buffer in bytes.                              |

## Return Value

Returns the number of bytes actually copied, or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

User has to provide a preallocated buffer where descriptor will be copied
to. The recommended size for a preallocated buffer is 4096 bytes.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

