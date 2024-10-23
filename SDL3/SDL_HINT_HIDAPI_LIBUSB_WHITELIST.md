###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_HIDAPI_LIBUSB_WHITELIST

A variable to control whether HIDAPI uses libusb only for whitelisted devices.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_LIBUSB_WHITELIST "SDL_HIDAPI_LIBUSB_WHITELIST"
```

## Remarks

By default libusb will only be used for a few devices that require direct
USB access.

The variable can be set to the following values:

- "0": HIDAPI will use libusb for all device access.
- "1": HIDAPI will use libusb only for whitelisted devices. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

