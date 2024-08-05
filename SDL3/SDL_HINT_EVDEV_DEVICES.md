###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_EVDEV_DEVICES

A variable containing a list of evdev devices to use if udev is not available.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EVDEV_DEVICES "SDL_EVDEV_DEVICES"
```

## Remarks

The list of devices is in the form:

deviceclass:path[,deviceclass:path[,...]]

where device class is an integer representing the
[SDL_UDEV_deviceclass](SDL_UDEV_deviceclass) and path is the full path to
the event device.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

