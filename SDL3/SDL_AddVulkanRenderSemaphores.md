###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AddVulkanRenderSemaphores

Add a set of synchronization semaphores for the current frame.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_AddVulkanRenderSemaphores(SDL_Renderer *renderer, Uint32 wait_stage_mask, Sint64 wait_semaphore, Sint64 signal_semaphore);

```

## Function Parameters

|                          |                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------- |
| **renderer**             | the rendering context                                                                                   |
| **wait_stage_mask**      | the VkPipelineStageFlags for the wait                                                                   |
| **wait_semaphore**       | a VkSempahore to wait on before rendering the current frame, or 0 if not needed                         |
| **signal_semaphore**     | a VkSempahore that SDL will signal when rendering for the current frame is complete, or 0 if not needed |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The Vulkan renderer will wait for `wait_semaphore` before submitting
rendering commands and signal `signal_semaphore` after rendering commands
are complete for this frame.

This should be called each frame that you want semaphore synchronization.
The Vulkan renderer may have multiple frames in flight on the GPU, so you
should have multiple semaphores that are used for synchronization. Querying
[SDL_PROP_RENDERER_VULKAN_SWAPCHAIN_IMAGE_COUNT_NUMBER](SDL_PROP_RENDERER_VULKAN_SWAPCHAIN_IMAGE_COUNT_NUMBER)
will give you the maximum number of semaphores you'll need.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

