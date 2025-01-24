# SDL_GetNumAllocations

Get the number of outstanding (unfreed) allocations.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_GetNumAllocations(void);
```

## Return Value

(int) Returns the number of allocations or -1 if allocation counting is
disabled.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

