###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Metal_DestroyView

Destroy an existing [SDL_MetalView](SDL_MetalView.md) object.

## Syntax

```c
void SDL_Metal_DestroyView(SDL_MetalView view);

```

## Function Parameters

|              |                                           |
| ------------ | ----------------------------------------- |
| **view**     | the [SDL_MetalView](SDL_MetalView.md) object |

## Remarks

This should be called before [SDL_DestroyWindow](SDL_DestroyWindow.md), if
[SDL_Metal_CreateView](SDL_Metal_CreateView.md) was called after
[SDL_CreateWindow](SDL_CreateWindow.md).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_Metal_CreateView](SDL_Metal_CreateView.md)

----
[CategoryAPI](CategoryAPI.md)
