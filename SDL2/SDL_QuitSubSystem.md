###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QuitSubSystem

Shut down specific SDL subsystems.

## Header File

Defined in [SDL.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL.h)

## Syntax

```c
void SDL_QuitSubSystem(Uint32 flags);
```

## Function Parameters

|        |           |                                                                                        |
| ------ | --------- | -------------------------------------------------------------------------------------- |
| Uint32 | **flags** | any of the flags used by [SDL_Init](SDL_Init)(); see [SDL_Init](SDL_Init) for details. |

## Remarks

If you start a subsystem using a call to that subsystem's init function
(for example [SDL_VideoInit](SDL_VideoInit)()) instead of
[SDL_Init](SDL_Init)() or [SDL_InitSubSystem](SDL_InitSubSystem)(),
[SDL_QuitSubSystem](SDL_QuitSubSystem)() and [SDL_WasInit](SDL_WasInit)()
will not work. You will need to use that subsystem's quit function
([SDL_VideoQuit](SDL_VideoQuit)()) directly instead. But generally, you
should not be using those functions directly anyhow; use
[SDL_Init](SDL_Init)() instead.

You still need to call [SDL_Quit](SDL_Quit)() even if you close all open
subsystems with [SDL_QuitSubSystem](SDL_QuitSubSystem)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_InitSubSystem](SDL_InitSubSystem)
- [SDL_Quit](SDL_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

