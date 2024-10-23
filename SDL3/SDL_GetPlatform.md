###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetPlatform

Get the name of the platform.

## Header File

Defined in [<SDL3/SDL_platform.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_platform.h)

## Syntax

```c
const char * SDL_GetPlatform(void);
```

## Return Value

(const char *) Returns the name of the platform. If the correct platform
name is not available, returns a string beginning with the text "Unknown".

## Remarks

Here are the names returned for some (but not all) supported platforms:

- "Windows"
- "macOS"
- "Linux"
- "iOS"
- "Android"

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPlatform](CategoryPlatform)

