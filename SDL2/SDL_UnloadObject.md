# SDL_UnloadObject

Unload a shared object from memory.

## Header File

Defined in [SDL_loadso.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_loadso.h)

## Syntax

```c
void SDL_UnloadObject(void *handle);
```

## Function Parameters

|        |            |                                                                              |
| ------ | ---------- | ---------------------------------------------------------------------------- |
| void * | **handle** | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject)(). |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LoadFunction](SDL_LoadFunction)
- [SDL_LoadObject](SDL_LoadObject)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLoadSO](CategoryLoadSO)

