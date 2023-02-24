###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadObject

Dynamically load a shared object.

## Syntax

```c
void* SDL_LoadObject(const char *sofile);

```

## Function Parameters

|                |                                            |
| -------------- | ------------------------------------------ |
| **sofile**     | a system-dependent name of the object file |

## Return Value

Returns an opaque pointer to the object handle or NULL if there was an
error; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadFunction](SDL_LoadFunction)
* [SDL_UnloadObject](SDL_UnloadObject)

----
[CategoryAPI](CategoryAPI)

