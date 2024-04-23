###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPlatform

Get the name of the platform.

## Header File

Defined in [SDL_platform.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_platform.h)

## Syntax

```c
const char * SDL_GetPlatform (void);

```

## Return Value

Returns the name of the platform. If the correct platform name is not
available, returns a string beginning with the text "Unknown".

## Remarks

Here are the names returned for some (but not all) supported platforms:

- "Windows"
- "Mac OS X"
- "Linux"
- "iOS"
- "Android"

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

