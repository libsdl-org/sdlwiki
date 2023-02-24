###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Metal_GetLayer

Get a pointer to the backing CAMetalLayer for the given view.

## Syntax

```c
void* SDL_Metal_GetLayer(SDL_MetalView view);

```

## Function Parameters

|              |                                           |
| ------------ | ----------------------------------------- |
| **view**     | the [SDL_MetalView](SDL_MetalView) object |

## Return Value

Returns a pointer

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_Metal_CreateView](SDL_Metal_CreateView)

----
[CategoryAPI](CategoryAPI)

