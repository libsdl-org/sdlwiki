###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Metal_DestroyView

Destroy an existing [SDL_MetalView](SDL_MetalView.md) object.

## Syntax

```c
void SDL_Metal_DestroyView(SDL_MetalView view);

```

## Remarks

This should be called before [SDL_DestroyWindow](SDL_DestroyWindow.md), if
[SDL_Metal_CreateView](SDL_Metal_CreateView.md) was called after
[SDL_CreateWindow](SDL_CreateWindow.md).

## Version

This function is available since SDL 2.0.12.

## Related Functions

* [SDL_Metal_CreateView](SDL_Metal_CreateView.md)

----
[CategoryAPI](CategoryAPI.md)
