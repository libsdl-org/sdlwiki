###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateThread

Create a new thread with a default stack size.

## Syntax

```c
extern DECLSPEC SDL_Thread *SDLCALL
SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);

```

## Function Parameters

|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| **fn**       | the [SDL_ThreadFunction](SDL_ThreadFunction.md) function to call in the new thread |
| **name**     | the name of the thread                                                          |
| **data**     | a pointer that is passed to `fn`                                                |

## Return Value

Returns an opaque pointer to the new thread object on success, NULL if the
new thread could not be created; call [SDL_GetError](SDL_GetError.md)() for
more information.

## Remarks

This is equivalent to calling:

```c
SDL_CreateThreadWithStackSize(fn, name, 0, data);
```

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateThreadWithStackSize](SDL_CreateThreadWithStackSize.md)
* [SDL_WaitThread](SDL_WaitThread.md)

----
[CategoryAPI](CategoryAPI.md)
