# SDL_HINT_HIDAPI_LIBUSB

A variable to control whether HIDAPI uses libusb for device access.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_LIBUSB "SDL_HIDAPI_LIBUSB"
```

## Remarks

By default libusb will only be used for a few devices that require direct
USB access, and this can be controlled with
[SDL_HINT_HIDAPI_LIBUSB_WHITELIST](SDL_HINT_HIDAPI_LIBUSB_WHITELIST).

The variable can be set to the following values:

- "0": HIDAPI will not use libusb for device access.
- "1": HIDAPI will use libusb for device access if available. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

