###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_HIDAPI_IGNORE_DEVICES

A variable containing a list of devices to ignore in [SDL_hid_enumerate](SDL_hid_enumerate)()

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_IGNORE_DEVICES "SDL_HIDAPI_IGNORE_DEVICES"
```

## Remarks

For example, to ignore the Shanwan DS3 controller and any Valve controller,
you might have the string "0x2563/0x0523,0x28de/0x0000"

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

