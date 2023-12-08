###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_read

Read an Input report from a HID device.

## Syntax

```c
int SDL_hid_read(SDL_hid_device *dev, unsigned char *data, size_t length);

```

## Function Parameters

|                |                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **dev**        | A device handle returned from [SDL_hid_open](SDL_hid_open.md)().                                                          |
| **data**       | A buffer to put the read data into.                                                                                    |
| **length**     | The number of bytes to read. For devices with multiple reports, make sure to read an extra byte for the report number. |

## Return Value

Returns the actual number of bytes read and -1 on error. If no packet was
available to be read and the handle is in non-blocking mode, this function
returns 0.

## Remarks

Input reports are returned to the host through the INTERRUPT IN endpoint.
The first byte will contain the Report number if the device uses numbered
reports.

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI.md)
