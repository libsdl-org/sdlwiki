###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUPresentMode

Specifies the timing that will be used to present swapchain textures to the OS.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUPresentMode
{
    SDL_GPU_PRESENTMODE_VSYNC,
    SDL_GPU_PRESENTMODE_IMMEDIATE,
    SDL_GPU_PRESENTMODE_MAILBOX
} SDL_GPUPresentMode;
```

## Remarks

Note that this value affects the behavior of
[SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture). VSYNC
mode will always be supported. IMMEDIATE and MAILBOX modes may not be
supported on certain systems.

It is recommended to query
[SDL_WindowSupportsGPUPresentMode](SDL_WindowSupportsGPUPresentMode) after
claiming the window if you wish to change the present mode to IMMEDIATE or
MAILBOX.

- VSYNC: Waits for vblank before presenting. No tearing is possible. If
  there is a pending image to present, the new image is enqueued for
  presentation. Disallows tearing at the cost of visual latency. When using
  this present mode, AcquireGPUSwapchainTexture will block if too many
  frames are in flight.
- IMMEDIATE: Immediately presents. Lowest latency option, but tearing may
  occur. When using this mode, AcquireGPUSwapchainTexture will fill the swapchain texture pointer with NULL
  if too many frames are in flight.
- MAILBOX: Waits for vblank before presenting. No tearing is possible. If
  there is a pending image to present, the pending image is replaced by the
  new image. Similar to VSYNC, but with reduced visual latency. When using
  this mode, AcquireGPUSwapchainTexture will fill the swapchain texture pointer with NULL if too many frames
  are in flight.

## Version

This enum is available since SDL 3.1.3

## See Also

- [SDL_SetGPUSwapchainParameters](SDL_SetGPUSwapchainParameters)
- [SDL_WindowSupportsGPUPresentMode](SDL_WindowSupportsGPUPresentMode)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

