###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LoadFunction](SDL_LoadFunction.md)
* [SDL_LoadObject](SDL_LoadObject.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySharedObject](CategorySharedObject.md)
