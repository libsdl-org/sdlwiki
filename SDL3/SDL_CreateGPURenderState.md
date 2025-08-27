# SDL_CreateGPURenderState

Create custom GPU render state.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
SDL_GPURenderState * SDL_CreateGPURenderState(SDL_Renderer *renderer, SDL_GPURenderStateCreateInfo *createinfo);
```

## Function Parameters

|                                                                |                |                                                     |
| -------------------------------------------------------------- | -------------- | --------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *                                 | **renderer**   | the renderer to use.                                |
| [SDL_GPURenderStateCreateInfo](SDL_GPURenderStateCreateInfo) * | **createinfo** | a struct describing the GPU render state to create. |

## Return Value

([SDL_GPURenderState](SDL_GPURenderState) *) Returns a custom GPU render
state or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_SetGPURenderStateFragmentUniforms](SDL_SetGPURenderStateFragmentUniforms)
- [SDL_SetRenderGPUState](SDL_SetRenderGPUState)
- [SDL_DestroyGPURenderState](SDL_DestroyGPURenderState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

