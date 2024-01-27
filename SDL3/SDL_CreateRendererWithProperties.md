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
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

These are the supported properties:

- [`SDL_PROP_RENDERER_CREATE_WINDOW_POINTER`](SDL_PROP_RENDERER_CREATE_WINDOW_POINTER):
  the window where rendering is displayed
- [`SDL_PROP_RENDERER_CREATE_SURFACE_POINTER`](SDL_PROP_RENDERER_CREATE_SURFACE_POINTER):
  the surface where rendering is displayed, if you want a software renderer
  without a window
- [`SDL_PROP_RENDERER_CREATE_NAME_STRING`](SDL_PROP_RENDERER_CREATE_NAME_STRING):
  the name of the rendering driver to use, if a specific one is desired
- [`SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_BOOLEAN`](SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_BOOLEAN):
  true if you want present synchronized with the refresh rate

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRenderer](SDL_CreateRenderer)
* [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)
* [SDL_DestroyRenderer](SDL_DestroyRenderer)
* [SDL_GetRendererInfo](SDL_GetRendererInfo)

----
[CategoryAPI](CategoryAPI)

