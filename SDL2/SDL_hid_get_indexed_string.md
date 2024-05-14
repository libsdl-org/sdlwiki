###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_get_indexed_string

Get a string from a HID device, based on its string index.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
int SDL_hid_get_indexed_string(SDL_hid_device *dev, int string_index, wchar_t *string, size_t maxlen);

```

## Function Parameters

|                      |                                                               |
| -------------------- | ------------------------------------------------------------- |
| **dev**              | A device handle returned from [SDL_hid_open](SDL_hid_open)(). |
| **string_index**     | The index of the string to get.                               |
| **string**           | A wide string buffer to put the data into.                    |
| **maxlen**           | The length of the buffer in multiples of wchar_t.             |

## Return Value

Returns 0 on success and -1 on error.

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

