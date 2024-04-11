###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Quit

Clean up all initialized subsystems.

## Header File

Defined in [SDL.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_Quit(void);

```

## Remarks

You should call this function even if you have already shutdown each
initialized subsystem with [SDL_QuitSubSystem](SDL_QuitSubSystem)(). It is
safe to call this function even in the case of errors in initialization.

If you start a subsystem using a call to that subsystem's init function
(for example [SDL_VideoInit](SDL_VideoInit)()) instead of
[SDL_Init](SDL_Init)() or [SDL_InitSubSystem](SDL_InitSubSystem)(), then
you must use that subsystem's quit function
([SDL_VideoQuit](SDL_VideoQuit)()) to shut it down before calling
[SDL_Quit](SDL_Quit)(). But generally, you should not be using those
functions directly anyhow; use [SDL_Init](SDL_Init)() instead.

You can use this function with atexit() to ensure that it is run when your
application is shutdown, but it is not wise to do this from a library or
other dynamically loaded code.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_Init](SDL_Init)
* [SDL_QuitSubSystem](SDL_QuitSubSystem)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)


