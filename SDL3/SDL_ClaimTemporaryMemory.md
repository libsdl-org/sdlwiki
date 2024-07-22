###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ClaimTemporaryMemory

Claim ownership of temporary memory.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void * SDL_ClaimTemporaryMemory(const void *mem);
```

## Function Parameters

|              |         |                                                                                        |
| ------------ | ------- | -------------------------------------------------------------------------------------- |
| const void * | **mem** | a pointer allocated with [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)(). |

## Return Value

(void *) Returns a pointer to the memory now owned by the application,
which must be freed using [SDL_free](SDL_free)(), or NULL if the memory is
not temporary or is not owned by this thread.

## Remarks

Some functions return temporary memory which SDL will automatically clean
up. If you want to hold onto it for a long time or beyond the current
function scope, you can call this function to get a pointer that you own,
and can free using [SDL_free](SDL_free)() when you're done.

If the memory isn't temporary, this will return NULL, and you don't have
ownership of the memory.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AllocateTemporaryMemory](SDL_AllocateTemporaryMemory)
- [SDL_free](SDL_free)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

