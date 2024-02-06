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

- [`SDL_PROP_RENDERER_CREATE_NAME_STRING`](SDL_PROP_RENDERER_CREATE_NAME_STRING):
  the name of the rendering driver to use, if a specific one is desired
- [`SDL_PROP_RENDERER_CREATE_WINDOW_POINTER`](SDL_PROP_RENDERER_CREATE_WINDOW_POINTER):
  the window where rendering is displayed, required if this isn't a
  software renderer using a surface
- [`SDL_PROP_RENDERER_CREATE_SURFACE_POINTER`](SDL_PROP_RENDERER_CREATE_SURFACE_POINTER):
  the surface where rendering is displayed, if you want a software renderer
  without a window
- [`SDL_PROP_RENDERER_CREATE_OUTPUT_COLORSPACE_NUMBER`](SDL_PROP_RENDERER_CREATE_OUTPUT_COLORSPACE_NUMBER):
  an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace for
  output to the display, defaults to
  [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB). The direct3d11 and direct3d12
  renderers support [SDL_COLORSPACE_SCRGB](SDL_COLORSPACE_SCRGB), which is
  a linear color space and supports HDR output. If you select
  [SDL_COLORSPACE_SCRGB](SDL_COLORSPACE_SCRGB), drawing still uses the sRGB
  colorspace, but values can go beyond 1.0 and float (linear) format
  textures can be used for HDR content.
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

