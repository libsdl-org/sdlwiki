###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockProperties

Unlock a set of properties.

## Header File

Defined in [SDL_properties.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_UnlockProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                          |
| ------------- | ------------------------ |
| **props**     | the properties to unlock |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_LockProperties](SDL_LockProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

