# SDL_GDKSuspendComplete

Callback from the application to let the suspend continue.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
void SDL_GDKSuspendComplete(void);
```

## Remarks

This should be called from an event watch in response to an
[`SDL_EVENT_DID_ENTER_BACKGROUND`](SDL_EVENT_DID_ENTER_BACKGROUND) event.

When using [SDL_Render](SDL_Render), your event watch should be added _after_ creating the [`SDL_Renderer`](SDL_Renderer); this allows the timing of the D3D12 command queue suspension to execute in the correct order.

When using [SDL_GPU](SDL_GPU), this should be called after calling [SDL_GDKSuspendGPU](SDL_GDKSuspendGPU).

If you're writing your own D3D12 renderer, this should be called after
calling `ID3D12CommandQueue::SuspendX`.

This function is only needed for Xbox GDK support; all other platforms will
do nothing and set an "unsupported" error message.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

