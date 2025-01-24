# SDL_LoadObject

Dynamically load a shared object.

## Header File

Defined in [<SDL3/SDL_loadso.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_loadso.h)

## Syntax

```c
SDL_SharedObject * SDL_LoadObject(const char *sofile);
```

## Function Parameters

|              |            |                                             |
| ------------ | ---------- | ------------------------------------------- |
| const char * | **sofile** | a system-dependent name of the object file. |

## Return Value

([SDL_SharedObject](SDL_SharedObject) *) Returns an opaque pointer to the
object handle or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LoadFunction](SDL_LoadFunction)
- [SDL_UnloadObject](SDL_UnloadObject)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySharedObject](CategorySharedObject)

