# SDL_UnloadObject

Unload a shared object from memory.

## Header File

Defined in [<SDL3/SDL_loadso.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_loadso.h)

## Syntax

```c
void SDL_UnloadObject(SDL_SharedObject *handle);
```

## Function Parameters

|                                        |            |                                                                              |
| -------------------------------------- | ---------- | ---------------------------------------------------------------------------- |
| [SDL_SharedObject](SDL_SharedObject) * | **handle** | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject)(). |

## Remarks

Note that any pointers from this object looked up through
[SDL_LoadFunction](SDL_LoadFunction)() will no longer be valid.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LoadObject](SDL_LoadObject)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySharedObject](CategorySharedObject)

