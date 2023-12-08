###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRenderDriverInfo

Get info about a specific 2D rendering driver for the current display.

## Syntax

```c
int SDL_GetRenderDriverInfo(int index,
                            SDL_RendererInfo * info);

```

## Function Parameters

|               |                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| **index**     | the index of the driver to query information about                                                      |
| **info**      | an [SDL_RendererInfo](SDL_RendererInfo.md) structure to be filled with information on the rendering driver |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers.md)

----
[CategoryAPI](CategoryAPI.md)
