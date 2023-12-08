###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QuitSubSystem

Shut down specific SDL subsystems.

## Syntax

```c
void SDL_QuitSubSystem(Uint32 flags);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **flags**     | any of the flags used by [SDL_Init](SDL_Init.md)(); see [SDL_Init](SDL_Init.md) for details. |

## Remarks

If you start a subsystem using a call to that subsystem's init function
(for example [SDL_VideoInit](SDL_VideoInit.md)()) instead of
[SDL_Init](SDL_Init.md)() or [SDL_InitSubSystem](SDL_InitSubSystem.md)(),
[SDL_QuitSubSystem](SDL_QuitSubSystem.md)() and [SDL_WasInit](SDL_WasInit.md)()
will not work. You will need to use that subsystem's quit function
([SDL_VideoQuit](SDL_VideoQuit.md)()) directly instead. But generally, you
should not be using those functions directly anyhow; use
[SDL_Init](SDL_Init.md)() instead.

You still need to call [SDL_Quit](SDL_Quit.md)() even if you close all open
subsystems with [SDL_QuitSubSystem](SDL_QuitSubSystem.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_InitSubSystem](SDL_InitSubSystem.md)
* [SDL_Quit](SDL_Quit.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
