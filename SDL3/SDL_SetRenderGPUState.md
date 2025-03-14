# SDL_SetRenderGPUState

Set custom GPU render state.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetRenderGPUState(SDL_Renderer *renderer, SDL_GPURenderState *state);
```

## Function Parameters

|                                            |              |                                                                |
| ------------------------------------------ | ------------ | -------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) *             | **renderer** | the renderer to use.                                           |
| [SDL_GPURenderState](SDL_GPURenderState) * | **state**    | the state to to use, or NULL to clear custom GPU render state. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets custom GPU render state for subsequent draw calls. This
allows using custom shaders with the GPU renderer.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

