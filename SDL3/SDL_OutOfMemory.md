# SDL_OutOfMemory

Set an error indicating that memory allocation failed.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
bool SDL_OutOfMemory(void);
```

## Return Value

(bool) Returns false.

## Remarks

This function does not do any memory allocation.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

