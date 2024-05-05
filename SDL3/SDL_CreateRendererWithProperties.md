###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateRendererWithProperties

Create a 2D rendering context for a window, with the specified properties.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

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
  [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB). The direct3d11, direct3d12,
  and metal renderers support
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR), which is a
  linear color space and supports HDR output. If you select
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR), drawing still
  uses the sRGB colorspace, but values can go beyond 1.0 and float (linear)
  format textures can be used for HDR content.
- [`SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_BOOLEAN`](SDL_PROP_RENDERER_CREATE_PRESENT_VSYNC_BOOLEAN):
  true if you want present synchronized with the refresh rate

With the vulkan renderer:

- [`SDL_PROP_RENDERER_CREATE_VULKAN_INSTANCE_POINTER`](SDL_PROP_RENDERER_CREATE_VULKAN_INSTANCE_POINTER):
  the VkInstance to use with the renderer, optional.
- [`SDL_PROP_RENDERER_CREATE_VULKAN_SURFACE_NUMBER`](SDL_PROP_RENDERER_CREATE_VULKAN_SURFACE_NUMBER):
  the VkSurfaceKHR to use with the renderer, optional.
- [`SDL_PROP_RENDERER_CREATE_VULKAN_PHYSICAL_DEVICE_POINTER`](SDL_PROP_RENDERER_CREATE_VULKAN_PHYSICAL_DEVICE_POINTER):
  the VkPhysicalDevice to use with the renderer, optional.
- [`SDL_PROP_RENDERER_CREATE_VULKAN_DEVICE_POINTER`](SDL_PROP_RENDERER_CREATE_VULKAN_DEVICE_POINTER):
  the VkDevice to use with the renderer, optional.
- [`SDL_PROP_RENDERER_CREATE_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER`](SDL_PROP_RENDERER_CREATE_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER):
  the queue family index used for rendering.
- [`SDL_PROP_RENDERER_CREATE_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER`](SDL_PROP_RENDERER_CREATE_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER):
  the queue family index used for presentation.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProperties](SDL_CreateProperties)
- [SDL_CreateRenderer](SDL_CreateRenderer)
- [SDL_CreateSoftwareRenderer](SDL_CreateSoftwareRenderer)
- [SDL_DestroyRenderer](SDL_DestroyRenderer)
- [SDL_GetRendererInfo](SDL_GetRendererInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

