###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FreeTemporaryMemory

Free temporary memory for the current thread.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_FreeTemporaryMemory(void);
```

## Remarks

This function frees all temporary memory for the current thread. If you
would like to hold onto a specific pointer beyond this call, you should
call [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)() to move it out
of the temporary memory pool.

This function is automatically called in [SDL_Quit](SDL_Quit)() on the main
thread and in [SDL_CleanupTLS](SDL_CleanupTLS)() when other threads
complete.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)
- [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

