# SDL_InitSubSystem

Compatibility function to initialize the SDL library.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
bool SDL_InitSubSystem(SDL_InitFlags flags);
```

## Function Parameters

|                                |           |                                                                                        |
| ------------------------------ | --------- | -------------------------------------------------------------------------------------- |
| [SDL_InitFlags](SDL_InitFlags) | **flags** | any of the flags used by [SDL_Init](SDL_Init)(); see [SDL_Init](SDL_Init) for details. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function and [SDL_Init](SDL_Init)() are interchangeable.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_Init](SDL_Init)
- [SDL_Quit](SDL_Quit)
- [SDL_QuitSubSystem](SDL_QuitSubSystem)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

