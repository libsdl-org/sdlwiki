# SDL_CreateGPURenderer

Create a 2D GPU rendering context.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Renderer * SDL_CreateGPURenderer(SDL_GPUDevice *device, SDL_Window *window);
```

## Function Parameters

|                                  |            |                                                                                   |
| -------------------------------- | ---------- | --------------------------------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | the GPU device to use with the renderer, or NULL to create a device.              |
| [SDL_Window](SDL_Window) *       | **window** | the window where rendering is displayed, or NULL to create an offscreen renderer. |

## Return Value

([SDL_Renderer](SDL_Renderer) *) Returns a valid rendering context or NULL
if there was an error; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The GPU device to use is passed in as a parameter. If this is NULL, then a
device will be created normally and can be retrieved using
[SDL_GetGPURendererDevice](SDL_GetGPURendererDevice)().

The window to use is passed in as a parameter. If this is NULL, then this
will become an offscreen renderer. In that case, you should call
[SDL_SetRenderTarget](SDL_SetRenderTarget)() to setup rendering to a
texture, and then call [SDL_RenderPresent](SDL_RenderPresent)() normally to
complete drawing a frame.

## Thread Safety

If this function is called with a valid GPU device, it should be called on
the thread that created the device. If this function is called with a valid
window, it should be called on the thread that created the window.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_CreateRendererWithProperties](SDL_CreateRendererWithProperties)
- [SDL_GetGPURendererDevice](SDL_GetGPURendererDevice)
- [SDL_CreateGPUShader](SDL_CreateGPUShader)
- [SDL_CreateGPURenderState](SDL_CreateGPURenderState)
- [SDL_SetGPURenderState](SDL_SetGPURenderState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

