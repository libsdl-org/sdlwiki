###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UnloadObject

Unload a shared object from memory.

## Header File

Defined in [<SDL3/SDL_loadso.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_loadso.h)

## Syntax

```c
void SDL_UnloadObject(void *handle);
```

## Function Parameters

|        |            |                                                                             |
| ------ | ---------- | --------------------------------------------------------------------------- |
| void * | **handle** | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject)() |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_LoadObject](SDL_LoadObject)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySharedObject](CategorySharedObject)

