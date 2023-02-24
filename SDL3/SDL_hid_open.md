###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_open

Open a HID device using a Vendor ID (VID), Product ID (PID) and optionally a serial number.

## Syntax

```c
SDL_hid_device * SDL_hid_open(unsigned short vendor_id, unsigned short product_id, const wchar_t *serial_number);

```

## Function Parameters

|                       |                                                            |
| --------------------- | ---------------------------------------------------------- |
| **vendor_id**         | The Vendor ID (VID) of the device to open.                 |
| **product_id**        | The Product ID (PID) of the device to open.                |
| **serial_number**     | The Serial Number of the device to open (Optionally NULL). |

## Return Value

Returns a pointer to a [SDL_hid_device](SDL_hid_device) object on success
or NULL on failure.

## Remarks

If `serial_number` is NULL, the first device with the specified VID and PID
is opened.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

