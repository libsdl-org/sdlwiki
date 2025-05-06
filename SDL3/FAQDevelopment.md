# FAQ: Development

## Do I `#include <SDL.h>` or `#include <SDL3/SDL.h>`?

The most portable way to include SDL headers is to use angular quotes around the full header name:

```c
#include <SDL3/SDL.h>
```

This is new in SDL3! Previously, in SDL2, we recommended `#include "SDL.h"`, but this proved to be unfriendly to macOS frameworks and having the API version in the include line is useful for making dependency requirements clear.

## How do I load images, sounds, show UI, etc?

SDL provides the lower level of functionality that a cross-platform game engine needs, leaving higher level tasks to other libraries. The [libraries page](Libraries) has a non-exhaustive list of libraries that are known to work well with SDL.

## Can I call SDL video functions from multiple threads?

No, most graphics back ends are not thread-safe, so you should only call SDL video functions from the main thread of your application. [SDL_RunOnMainThread()](SDL_RunOnMainThread) can be used to dispatch code that needs to run on the main thread.

## Can I call SDL event functions from multiple threads?

The main event handling should be done on the main thread, though you can use [SDL_PushEvent()](SDL_PushEvent) and [SDL_PeepEvents()](SDL_PeepEvents) to interact with the event queue on other threads. Most SDL functions have their thread-safety noted in their documentation.

## Can I use shaders with the SDL 2D render API?

No, there are many different ways to use shaders, and rather than restrict you to a subset of shader functionality, we recommend using a full 3D API like [SDL GPU](CategoryGPU). You can look at how SDL uses the GPU API for 2D rendering if you'd like to expand on that: [SDL_render_gpu.c](https://github.com/libsdl-org/SDL/blob/main/src/render/gpu/SDL_render_gpu.c)
