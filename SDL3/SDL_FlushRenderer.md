###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlushRenderer

Force the rendering context to flush any pending commands and state.

## Syntax

```c
int SDL_FlushRenderer(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You do not need to (and in fact, shouldn't) call this function unless you
are planning to call into OpenGL/Direct3D/Metal/whatever directly, in
addition to using an [SDL_Renderer](SDL_Renderer).

This is for a very-specific case: if you are using SDL's render API, and
you plan to make OpenGL/D3D/whatever calls in addition to SDL render API
calls. If this applies, you should call this function between calls to
SDL's render API and the low-level API you're using in cooperation.

In all other cases, you can ignore this function.

This call makes SDL flush any pending rendering work it was queueing up to
do later in a single batch, and marks any internal cached state as invalid,
so it'll prepare all its state again later, from scratch.

This means you do not need to save state in your rendering code to protect
the SDL renderer. However, there lots of arbitrary pieces of Direct3D and
OpenGL state that can confuse things; you should use your best judgement
and be prepared to make changes if specific state needs to be protected.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

