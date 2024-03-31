###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnlockSurface

Release a surface after directly accessing the pixels.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_UnlockSurface(SDL_Surface *surface);

```

## Function Parameters

|                 |                                                         |
| --------------- | ------------------------------------------------------- |
| **surface**     | the [SDL_Surface](SDL_Surface) structure to be unlocked |

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_LockSurface](SDL_LockSurface), , , from="== Code Examples ==", to="== Remarks ==")>>

## Related Functions

* [SDL_LockSurface](SDL_LockSurface)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


