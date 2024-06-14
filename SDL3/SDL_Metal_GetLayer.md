###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Metal_GetLayer

Get a pointer to the backing CAMetalLayer for the given view.

## Header File

Defined in [<SDL3/SDL_metal.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_metal.h)

## Syntax

```c
void* SDL_Metal_GetLayer(SDL_MetalView view);
```

## Function Parameters

|                                |          |                                            |
| ------------------------------ | -------- | ------------------------------------------ |
| [SDL_MetalView](SDL_MetalView) | **view** | the [SDL_MetalView](SDL_MetalView) object. |

## Return Value

(void *) Returns a pointer.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMetal](CategoryMetal)

