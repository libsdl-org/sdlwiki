###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_enumerate

Enumerate the HID Devices.

## Syntax

```c
SDL_hid_device_info * SDL_hid_enumerate(unsigned short vendor_id, unsigned short product_id);

```

## Function Parameters

|                    |                                                                                 |
| ------------------ | ------------------------------------------------------------------------------- |
| **vendor_id**      | The Vendor ID (VID) of the types of device to open, or 0 to match any vendor.   |
| **product_id**     | The Product ID (PID) of the types of device to open, or 0 to match any product. |

## Return Value

Returns a pointer to a linked list of type
[SDL_hid_device_info](SDL_hid_device_info.md), containing information about
the HID devices attached to the system, or NULL in the case of failure.
Free this linked list by calling
[SDL_hid_free_enumeration](SDL_hid_free_enumeration.md)().

## Remarks

This function returns a linked list of all the HID devices attached to the
system which match vendor_id and product_id. If `vendor_id` is set to 0
then any vendor matches. If `product_id` is set to 0 then any product
matches. If `vendor_id` and `product_id` are both set to 0, then all HID
devices will be returned.

By default SDL will only enumerate controllers, to reduce risk of hanging
or crashing on bad drivers, but
[SDL_HINT_HIDAPI_ENUMERATE_ONLY_CONTROLLERS](SDL_HINT_HIDAPI_ENUMERATE_ONLY_CONTROLLERS.md)
can be set to "0" to enumerate all HID devices.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_hid_device_change_count](SDL_hid_device_change_count.md)

----
[CategoryAPI](CategoryAPI.md)
