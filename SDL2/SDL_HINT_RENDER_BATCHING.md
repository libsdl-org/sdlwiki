###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_BATCHING

A variable controlling whether the 2D render API is compatible or efficient.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_BATCHING  "SDL_RENDER_BATCHING"
```

## Remarks

This variable can be set to the following values:

- "0": Don't use batching to make rendering more efficient.
- "1": Use batching, but might cause problems if app makes its own direct
  OpenGL calls.

Up to SDL 2.0.9, the render API would draw immediately when requested. Now
it batches up draw requests and sends them all to the GPU only when forced
to (during [SDL_RenderPresent](SDL_RenderPresent), when changing render
targets, by updating a texture that the batch needs, etc). This is
significantly more efficient, but it can cause problems for apps that
expect to render on top of the render API's output. As such, SDL will
disable batching if a specific render backend is requested (since this
might indicate that the app is planning to use the underlying graphics API
directly). This hint can be used to explicitly request batching in this
instance. It is a contract that you will either never use the underlying
graphics API directly, or if you do, you will call
[SDL_RenderFlush](SDL_RenderFlush)() before you do so any current batch
goes to the GPU before your work begins. Not following this contract will
result in undefined behavior.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

