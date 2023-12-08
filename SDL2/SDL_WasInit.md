###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WasInit

Get a mask of the specified subsystems which are currently initialized.

## Syntax

```c
Uint32 SDL_WasInit(Uint32 flags);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **flags**     | any of the flags used by [SDL_Init](SDL_Init.md)(); see [SDL_Init](SDL_Init.md) for details. |

## Return Value

Returns a mask of all initialized subsystems if `flags` is 0, otherwise it
returns the initialization status of the specified subsystems.

The return value does not include
[SDL_INIT_NOPARACHUTE](SDL_INIT_NOPARACHUTE.md).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_Init](SDL_Init.md)
* [SDL_InitSubSystem](SDL_InitSubSystem.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
