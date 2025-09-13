# SDL_hid_open_path

Open a HID device by its path name.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
SDL_hid_device * SDL_hid_open_path(const char *path, int bExclusive);
```

## Function Parameters

|              |                |                                      |
| ------------ | -------------- | ------------------------------------ |
| const char * | **path**       | The path name of the device to open. |
| int          | **bExclusive** | boolean exclusive.                   |

## Return Value

([SDL_hid_device](SDL_hid_device) *) Returns a pointer to a
[SDL_hid_device](SDL_hid_device) object on success or NULL on failure.

## Remarks

The path name be determined by calling
[SDL_hid_enumerate](SDL_hid_enumerate)(), or a platform-specific path name
can be used (eg: /dev/hidraw0 on Linux).

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

