# SDL_HINT_HIDAPI_LIBUSB_GAMECUBE

A variable to control whether HIDAPI uses libusb for GameCube adapters.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_LIBUSB_GAMECUBE "SDL_HIDAPI_LIBUSB_GAMECUBE"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI will not use libusb for GameCube adapters.
- "1": HIDAPI will use libusb for GameCube adapters if available. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

