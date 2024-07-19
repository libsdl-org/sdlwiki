###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FreeTemporaryMemory

Free temporary memory.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_FreeTemporaryMemory(const void *mem);
```

## Function Parameters

|              |         |                                                                                                                                           |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| const void * | **mem** | a pointer allocated with [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)(), or NULL to free all pending temporary allocations. |

## Remarks

This function frees temporary memory allocated for events and functions
that return temporary memory. This memory is local to the thread that
creates it and is automatically freed for the main thread when processing
events. For other threads you may call this function periodically to free
any temporary memory created by that thread.

You can free a specific pointer, to provide more fine grained control over
memory management, or you can pass NULL to free all pending temporary
allocations.

All temporary memory is freed on the main thread in [SDL_Quit](SDL_Quit)()
and for other threads when they call [SDL_CleanupTLS](SDL_CleanupTLS)(),
which is automatically called at cleanup time for threads created using
[SDL_CreateThread](SDL_CreateThread)().

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

