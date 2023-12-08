###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_InitSubSystem

Compatibility function to initialize the SDL library.

## Syntax

```c
int SDL_InitSubSystem(Uint32 flags);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **flags**     | any of the flags used by [SDL_Init](SDL_Init.md)(); see [SDL_Init](SDL_Init.md) for details. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

In SDL2, this function and [SDL_Init](SDL_Init.md)() are interchangeable.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_Init](SDL_Init.md)
* [SDL_Quit](SDL_Quit.md)
* [SDL_QuitSubSystem](SDL_QuitSubSystem.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
