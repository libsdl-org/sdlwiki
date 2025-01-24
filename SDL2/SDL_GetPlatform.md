# SDL_GetPlatform

Get the name of the platform.

## Header File

Defined in [SDL_platform.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_platform.h)

## Syntax

```c
const char * SDL_GetPlatform (void);
```

## Return Value

(const char *) Returns the name of the platform. If the correct platform
name is not available, returns a string beginning with the text "Unknown".

## Remarks

Here are the names returned for some (but not all) supported platforms:

- "Windows"
- "Mac OS X"
- "Linux"
- "iOS"
- "Android"

## Version

This function is available since SDL 2.0.0.

## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPlatform](CategoryPlatform)

