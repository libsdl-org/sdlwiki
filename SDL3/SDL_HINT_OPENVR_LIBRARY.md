###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_OPENVR_LIBRARY

Mechanism to specify openvr_api library location

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_OPENVR_LIBRARY              "SDL_OPENVR_LIBRARY"
```

## Remarks

By default, when using the OpenVR driver, it will search for the API
library in the current folder. But, if you wish to use a system API you can
specify that by using this hint. This should be the full or relative path
to a .dll on Windows or .so on Linux.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

