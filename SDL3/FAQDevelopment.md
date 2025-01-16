# FAQ: Development

## Do I `#include <SDL.h>` or `#include <SDL3/SDL.h>`?

The most portable way to include SDL headers is to use angular quotes around the full header name:

```c
#include <SDL3/SDL.h>
```

This is new in SDL3! Previously, in SDL2, we recommended `#include "SDL.h"`, but this proved to be unfriendly to macOS frameworks and having the API version in the include line is useful for making dependency requirements clear.

## Can I call SDL video functions from multiple threads?

No, most graphics back ends are not thread-safe, so you should only call SDL video functions from the main thread of your application. [SDL_RunOnMainThread()](SDL_RunOnMainThread) can be used to dispatch code that needs to run on the main thread.

## Can I call SDL event functions from multiple threads?

The main event handling should be done on the main thread, though you can use [SDL_PushEvent()](SDL_PushEvent) and [SDL_PeepEvents()](SDL_PeepEvents) to interact with the event queue on other threads. Most SDL functions have their thread-safety noted in their documentation.

## How do I load images, sounds, display UI, etc?

SDL provides the lower level of functionality that a cross-platform game engine needs, leaving higher level tasks to other libraries. The [libraries page](Libraries) has a non-exhaustive list of libraries that are known to work well with SDL.
