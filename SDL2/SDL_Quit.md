###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Quit

Clean up all initialized subsystems.

## Syntax

```c
void SDL_Quit(void);

```

## Remarks

You should call this function even if you have already shutdown each
initialized subsystem with [SDL_QuitSubSystem](SDL_QuitSubSystem.md)(). It is
safe to call this function even in the case of errors in initialization.

If you start a subsystem using a call to that subsystem's init function
(for example [SDL_VideoInit](SDL_VideoInit.md)()) instead of
[SDL_Init](SDL_Init.md)() or [SDL_InitSubSystem](SDL_InitSubSystem.md)(), then
you must use that subsystem's quit function
([SDL_VideoQuit](SDL_VideoQuit.md)()) to shut it down before calling
[SDL_Quit](SDL_Quit.md)(). But generally, you should not be using those
functions directly anyhow; use [SDL_Init](SDL_Init.md)() instead.

You can use this function with atexit() to ensure that it is run when your
application is shutdown, but it is not wise to do this from a library or
other dynamically loaded code.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_Init](SDL_Init.md)
* [SDL_QuitSubSystem](SDL_QuitSubSystem.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
