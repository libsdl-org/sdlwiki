###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnloadObject

Unload a shared object from memory.

## Syntax

```c
void SDL_UnloadObject(void *handle);

```

## Function Parameters

|                |                                                                             |
| -------------- | --------------------------------------------------------------------------- |
| **handle**     | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject.md)() |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadFunction](SDL_LoadFunction.md)
* [SDL_LoadObject](SDL_LoadObject.md)

----
[CategoryAPI](CategoryAPI.md)
