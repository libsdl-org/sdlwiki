###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_get_product_string

Get The Product String from a HID device.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
int SDL_hid_get_product_string(SDL_hid_device *dev, wchar_t *string, size_t maxlen);
```

## Function Parameters

|                                    |            |                                                               |
| ---------------------------------- | ---------- | ------------------------------------------------------------- |
| [SDL_hid_device](SDL_hid_device) * | **dev**    | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |
| wchar_t *                          | **string** | A wide string buffer to put the data into.                    |
| size_t                             | **maxlen** | The length of the buffer in multiples of wchar_t.             |

## Return Value

(int) Returns 0 on success and -1 on error.

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

