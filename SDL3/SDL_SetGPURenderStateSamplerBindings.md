# SDL_SetGPURenderStateSamplerBindings

Set sampler bindings variables in a custom GPU render state.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetGPURenderStateSamplerBindings(SDL_GPURenderState *state, int num_sampler_bindings, const SDL_GPUTextureSamplerBinding *sampler_bindings);
```

## Function Parameters

|                                                                      |                          |                                                     |
| -------------------------------------------------------------------- | ------------------------ | --------------------------------------------------- |
| [SDL_GPURenderState](SDL_GPURenderState) *                           | **state**                | the state to modify.                                |
| int                                                                  | **num_sampler_bindings** | The number of additional fragment samplers to bind. |
| const [SDL_GPUTextureSamplerBinding](SDL_GPUTextureSamplerBinding) * | **sampler_bindings**     | Additional fragment samplers to bind.               |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The data is copied and will be binded using
[SDL_BindGPUFragmentSamplers](SDL_BindGPUFragmentSamplers)() during draw
call execution.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

