###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPlatform

Get the name of the platform.

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
- "macOS"
- "Linux"
- "iOS"
- "Android"

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryPlatform](CategoryPlatform.md)
