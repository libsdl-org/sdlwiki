###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRendererProperties

Get the properties associated with a renderer.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_PropertiesID SDL_GetRendererProperties(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The following read-only properties are provided by SDL:

- [`SDL_PROP_RENDERER_NAME_STRING`](SDL_PROP_RENDERER_NAME_STRING): the
  name of the rendering driver
- [`SDL_PROP_RENDERER_WINDOW_POINTER`](SDL_PROP_RENDERER_WINDOW_POINTER):
  the window where rendering is displayed, if any
- [`SDL_PROP_RENDERER_SURFACE_POINTER`](SDL_PROP_RENDERER_SURFACE_POINTER):
  the surface where rendering is displayed, if this is a software renderer
  without a window
- [`SDL_PROP_RENDERER_VSYNC_NUMBER`](SDL_PROP_RENDERER_VSYNC_NUMBER): the
  current vsync setting
- [`SDL_PROP_RENDERER_MAX_TEXTURE_SIZE_NUMBER`](SDL_PROP_RENDERER_MAX_TEXTURE_SIZE_NUMBER):
  the maximum texture width and height
- [`SDL_PROP_RENDERER_TEXTURE_FORMATS_POINTER`](SDL_PROP_RENDERER_TEXTURE_FORMATS_POINTER):
  a (const [SDL_PixelFormatEnum](SDL_PixelFormatEnum) *) array of pixel
  formats, terminated with
  [SDL_PIXELFORMAT_UNKNOWN](SDL_PIXELFORMAT_UNKNOWN), representing the
  available texture formats for this renderer.
- [`SDL_PROP_RENDERER_OUTPUT_COLORSPACE_NUMBER`](SDL_PROP_RENDERER_OUTPUT_COLORSPACE_NUMBER):
  an [SDL_ColorSpace](SDL_ColorSpace) value describing the colorspace for
  output to the display, defaults to
  [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB).
- [`SDL_PROP_RENDERER_HDR_ENABLED_BOOLEAN`](SDL_PROP_RENDERER_HDR_ENABLED_BOOLEAN):
  true if the output colorspace is
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR) and the renderer
  is showing on a display with HDR enabled. This property can change
  dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.
- [`SDL_PROP_RENDERER_SDR_WHITE_POINT_FLOAT`](SDL_PROP_RENDERER_SDR_WHITE_POINT_FLOAT):
  the value of SDR white in the
  [SDL_COLORSPACE_SRGB_LINEAR](SDL_COLORSPACE_SRGB_LINEAR) colorspace. When
  HDR is enabled, this value is automatically multiplied into the color
  scale. This property can change dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.
- [`SDL_PROP_RENDERER_HDR_HEADROOM_FLOAT`](SDL_PROP_RENDERER_HDR_HEADROOM_FLOAT):
  the additional high dynamic range that can be displayed, in terms of the
  SDR white point. When HDR is not enabled, this will be 1.0. This property
  can change dynamically when
  [SDL_EVENT_DISPLAY_HDR_STATE_CHANGED](SDL_EVENT_DISPLAY_HDR_STATE_CHANGED)
  is sent.

With the direct3d renderer:

- [`SDL_PROP_RENDERER_D3D9_DEVICE_POINTER`](SDL_PROP_RENDERER_D3D9_DEVICE_POINTER):
  the IDirect3DDevice9 associated with the renderer

With the direct3d11 renderer:

- [`SDL_PROP_RENDERER_D3D11_DEVICE_POINTER`](SDL_PROP_RENDERER_D3D11_DEVICE_POINTER):
  the ID3D11Device associated with the renderer
- [`SDL_PROP_RENDERER_D3D11_SWAPCHAIN_POINTER`](SDL_PROP_RENDERER_D3D11_SWAPCHAIN_POINTER):
  the IDXGISwapChain1 associated with the renderer. This may change when
  the window is resized.

With the direct3d12 renderer:

- [`SDL_PROP_RENDERER_D3D12_DEVICE_POINTER`](SDL_PROP_RENDERER_D3D12_DEVICE_POINTER):
  the ID3D12Device associated with the renderer
- [`SDL_PROP_RENDERER_D3D12_SWAPCHAIN_POINTER`](SDL_PROP_RENDERER_D3D12_SWAPCHAIN_POINTER):
  the IDXGISwapChain4 associated with the renderer.
- [`SDL_PROP_RENDERER_D3D12_COMMAND_QUEUE_POINTER`](SDL_PROP_RENDERER_D3D12_COMMAND_QUEUE_POINTER):
  the ID3D12CommandQueue associated with the renderer

With the vulkan renderer:

- [`SDL_PROP_RENDERER_VULKAN_INSTANCE_POINTER`](SDL_PROP_RENDERER_VULKAN_INSTANCE_POINTER):
  the VkInstance associated with the renderer
- [`SDL_PROP_RENDERER_VULKAN_SURFACE_NUMBER`](SDL_PROP_RENDERER_VULKAN_SURFACE_NUMBER):
  the VkSurfaceKHR associated with the renderer
- [`SDL_PROP_RENDERER_VULKAN_PHYSICAL_DEVICE_POINTER`](SDL_PROP_RENDERER_VULKAN_PHYSICAL_DEVICE_POINTER):
  the VkPhysicalDevice associated with the renderer
- [`SDL_PROP_RENDERER_VULKAN_DEVICE_POINTER`](SDL_PROP_RENDERER_VULKAN_DEVICE_POINTER):
  the VkDevice associated with the renderer
- [`SDL_PROP_RENDERER_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER`](SDL_PROP_RENDERER_VULKAN_GRAPHICS_QUEUE_FAMILY_INDEX_NUMBER):
  the queue family index used for rendering
- [`SDL_PROP_RENDERER_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER`](SDL_PROP_RENDERER_VULKAN_PRESENT_QUEUE_FAMILY_INDEX_NUMBER):
  the queue family index used for presentation
- [`SDL_PROP_RENDERER_VULKAN_SWAPCHAIN_IMAGE_COUNT_NUMBER`](SDL_PROP_RENDERER_VULKAN_SWAPCHAIN_IMAGE_COUNT_NUMBER):
  the number of swapchain images, or potential frames in flight, used by
  the Vulkan renderer

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetProperty](SDL_GetProperty)
- [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

