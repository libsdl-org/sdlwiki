###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderFlush

Force the rendering context to flush any pending commands to the underlying rendering API.

## Syntax

```c
int SDL_RenderFlush(SDL_Renderer *renderer);

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
are planning to call into OpenGL/Direct3D/Metal/whatever directly in
addition to using an [SDL_Renderer](SDL_Renderer).

This is for a very-specific case: if you are using SDL's render API, you
asked for a specific renderer backend (OpenGL, Direct3D, etc), you set
[SDL_HINT_RENDER_BATCHING](SDL_HINT_RENDER_BATCHING) to "1", and you plan
to make OpenGL/D3D/whatever calls in addition to SDL render API calls. If
all of this applies, you should call [SDL_RenderFlush](SDL_RenderFlush)()
between calls to SDL's render API and the low-level API you're using in
cooperation.

In all other cases, you can ignore this function. This is only here to get
maximum performance out of a specific situation. In all other cases, SDL
will do the right thing, perhaps at a performance loss.

This function is first available in SDL 2.0.10, and is not needed in 2.0.9
and earlier, as earlier versions did not queue rendering commands at all,
instead flushing them to the OS immediately.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

