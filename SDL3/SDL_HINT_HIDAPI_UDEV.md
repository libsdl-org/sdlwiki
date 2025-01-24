# SDL_HINT_HIDAPI_UDEV

A variable to control whether HIDAPI uses udev for device detection.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_UDEV "SDL_HIDAPI_UDEV"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI will poll for device changes.
- "1": HIDAPI will use udev for device detection. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

