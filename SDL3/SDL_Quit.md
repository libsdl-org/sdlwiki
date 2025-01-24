# SDL_Quit

Clean up all initialized subsystems.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
void SDL_Quit(void);
```

## Remarks

You should call this function even if you have already shutdown each
initialized subsystem with [SDL_QuitSubSystem](SDL_QuitSubSystem)(). It is
safe to call this function even in the case of errors in initialization.

You can use this function with atexit() to ensure that it is run when your
application is shutdown, but it is not wise to do this from a library or
other dynamically loaded code.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_Init](SDL_Init)
- [SDL_QuitSubSystem](SDL_QuitSubSystem)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

