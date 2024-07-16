###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FreeEventMemory

Free temporary event memory allocated by SDL.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_FreeEventMemory(void);
```

## Remarks

This function frees temporary memory allocated for events and APIs that
return temporary strings. This memory is local to the thread that creates
it and is automatically freed for the main thread when pumping the event
loop. For other threads you may want to call this function periodically to
free any temporary memory created by that thread.

Note that if you call [SDL_AllocateEventMemory](SDL_AllocateEventMemory)()
on one thread and pass it to another thread, e.g. via a user event, then
you should be sure the other thread has finished processing it before
calling this function.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AllocateEventMemory](SDL_AllocateEventMemory)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

