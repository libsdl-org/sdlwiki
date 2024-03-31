###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPlatform

Get the name of the platform.

## Header File

Defined in [SDL_platform.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_platform.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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
[CategoryAPI](CategoryAPI), [CategoryPlatform](CategoryPlatform)


