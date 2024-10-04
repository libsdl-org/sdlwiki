###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_QuitSubSystem

Shut down specific SDL subsystems.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
void SDL_QuitSubSystem(SDL_InitFlags flags);
```

## Function Parameters

|                                |           |                                                                                        |
| ------------------------------ | --------- | -------------------------------------------------------------------------------------- |
| [SDL_InitFlags](SDL_InitFlags) | **flags** | any of the flags used by [SDL_Init](SDL_Init)(); see [SDL_Init](SDL_Init) for details. |

## Remarks

You still need to call [SDL_Quit](SDL_Quit)() even if you close all open
subsystems with [SDL_QuitSubSystem](SDL_QuitSubSystem)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_InitSubSystem](SDL_InitSubSystem)
- [SDL_Quit](SDL_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

