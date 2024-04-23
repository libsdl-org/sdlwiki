###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowWMInfo

Get driver-specific information about a window.

## Header File

Defined in [SDL_syswm.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_syswm.h)

## Syntax

```c
SDL_bool SDL_GetWindowWMInfo(SDL_Window * window,
                             SDL_SysWMinfo * info);

```

## Function Parameters

|                |                                                                               |
| -------------- | ----------------------------------------------------------------------------- |
| **window**     | the window about which information is being requested                         |
| **info**       | an [SDL_SysWMinfo](SDL_SysWMinfo) structure filled in with window information |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the function is implemented and the
`version` member of the `info` struct is valid, or [SDL_FALSE](SDL_FALSE)
if the information could not be retrieved; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You must include [SDL_syswm](SDL_syswm).h for the declaration of
[SDL_SysWMinfo](SDL_SysWMinfo).

The caller must initialize the `info` structure's version by using
`SDL_VERSION(&info.version)`, and then this function will fill in the rest
of the structure with information about the given window.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

