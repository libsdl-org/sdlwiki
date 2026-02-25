# SDL_GDKSuspendComplete

Callback from the application to let the suspend continue.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
void SDL_GDKSuspendComplete(void);
```

## Remarks

When using [SDL_Render](SDL_Render) or [SDL_GPU](SDL_GPU), this function
should be called _after_ creating the [`SDL_Renderer`](SDL_Renderer) or
[`SDL_GPUDevice`](SDL_GPUDevice); this allows the timing of the D3D12
command queue suspension to execute in the correct order.

If you're writing your own D3D12 renderer, this should be called after
calling `ID3D12CommandQueue::SuspendX`.

This function is only needed for Xbox GDK support; all other platforms will
do nothing and set an "unsupported" error message.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

