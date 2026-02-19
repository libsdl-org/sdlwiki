# SDL_GDKSuspendComplete

Callback from the application to let the suspend continue.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
void SDL_GDKSuspendComplete(void);
```

## Remarks

This function is only needed for Xbox GDK support; all other platforms will
do nothing and set an "unsupported" error message.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

