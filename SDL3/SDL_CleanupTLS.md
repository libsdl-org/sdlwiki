# SDL_CleanupTLS

Cleanup all TLS data for this thread.

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
void SDL_CleanupTLS(void);
```

## Remarks

If you are creating your threads outside of SDL and then calling SDL
functions, you should call this function before your thread exits, to
properly clean up SDL memory.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryThread](CategoryThread)

