# SDL_CreateGPURenderer

Create a 2D GPU rendering context for a window, with support for the specified shader format.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_Renderer * SDL_CreateGPURenderer(SDL_Window *window, SDL_GPUShaderFormat format_flags, SDL_GPUDevice **device);
```

## Function Parameters

|                                            |                  |                                                                       |
| ------------------------------------------ | ---------------- | --------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *                 | **window**       | the window where rendering is displayed.                              |
| [SDL_GPUShaderFormat](SDL_GPUShaderFormat) | **format_flags** | a bitflag indicating which shader formats the app is able to provide. |
| [SDL_GPUDevice](SDL_GPUDevice) **          | **device**       | a pointer filled with the associated GPU device, or NULL on error.    |

## Return Value

([SDL_Renderer](SDL_Renderer) *) Returns a valid rendering context or NULL
if there was an error; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This is a convenience function to create a SDL GPU backed renderer,
intended to be used with [SDL_GPURenderState](SDL_GPURenderState). The
resulting renderer will support shaders in one of the specified shader
formats.

If no available GPU driver supports any of the specified shader formats,
this function will fail.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_CreateRendererWithProperties](SDL_CreateRendererWithProperties)
- [SDL_GetGPUShaderFormats](SDL_GetGPUShaderFormats)
- [SDL_CreateGPUShader](SDL_CreateGPUShader)
- [SDL_CreateGPURenderState](SDL_CreateGPURenderState)
- [SDL_SetRenderGPUState](SDL_SetRenderGPUState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

