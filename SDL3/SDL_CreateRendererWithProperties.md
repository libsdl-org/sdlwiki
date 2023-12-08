###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateRendererWithProperties

Create a 2D rendering context for a window, with the specified properties.

## Syntax

```c
SDL_Renderer * SDL_CreateRendererWithProperties(SDL_PropertiesID props);

```

## Function Parameters

|               |                       |
| ------------- | --------------------- |
| **props**     | the properties to use |

## Return Value

Returns a valid rendering context or NULL if there was an error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

These are the supported properties:

- "window" (pointer) - the window where rendering is displayed
- "surface" (pointer) - the surface where rendering is displayed, if you
  want a software renderer without a window
- "name" (string) - the name of the rendering driver to use, if a specific
  one is desired
- "present_vsync" (boolean) - true if you want present synchronized with
  the refresh rate

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer.md)
* [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer.md)
* [SDL_DestroyRenderer](SDL_DestroyRenderer.md)
* [SDL_GetRendererInfo](SDL_GetRendererInfo.md)

----
[CategoryAPI](CategoryAPI.md)
