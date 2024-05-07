###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_enumerate

Enumerate the HID Devices.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
SDL_hid_device_info * SDL_hid_enumerate(unsigned short vendor_id, unsigned short product_id);

```

## Function Parameters

|                    |                                                      |
| ------------------ | ---------------------------------------------------- |
| **vendor_id**      | The Vendor ID (VID) of the types of device to open.  |
| **product_id**     | The Product ID (PID) of the types of device to open. |

## Return Value

Returns a pointer to a linked list of type
[SDL_hid_device_info](SDL_hid_device_info), containing information about
the HID devices attached to the system, or NULL in the case of failure.
Free this linked list by calling
[SDL_hid_free_enumeration](SDL_hid_free_enumeration)().

## Remarks

This function returns a linked list of all the HID devices attached to the
system which match vendor_id and product_id. If `vendor_id` is set to 0
then any vendor matches. If `product_id` is set to 0 then any product
matches. If `vendor_id` and `product_id` are both set to 0, then all HID
devices will be returned.

## Version

This function is available since SDL 2.0.18.

## See Also

- [SDL_hid_device_change_count](SDL_hid_device_change_count)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

