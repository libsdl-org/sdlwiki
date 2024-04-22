###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_HIDAPI_ENUMERATE_ONLY_CONTROLLERS

A variable to control whether [SDL_hid_enumerate](SDL_hid_enumerate)() enumerates all HID devices or only controllers.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_HIDAPI_ENUMERATE_ONLY_CONTROLLERS "SDL_HIDAPI_ENUMERATE_ONLY_CONTROLLERS"
```

## Remarks

The variable can be set to the following values:

- "0": [SDL_hid_enumerate](SDL_hid_enumerate)() will enumerate all HID
  devices.
- "1": [SDL_hid_enumerate](SDL_hid_enumerate)() will only enumerate
  controllers. (default)

By default SDL will only enumerate controllers, to reduce risk of hanging
or crashing on devices with bad drivers and avoiding macOS keyboard capture
permission prompts.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

