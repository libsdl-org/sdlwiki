# SDL_Metal_GetLayer

Get a pointer to the backing CAMetalLayer for the given view.

## Header File

Defined in [<SDL3/SDL_metal.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_metal.h)

## Syntax

```c
void * SDL_Metal_GetLayer(SDL_MetalView view);
```

## Function Parameters

|                                |          |                                            |
| ------------------------------ | -------- | ------------------------------------------ |
| [SDL_MetalView](SDL_MetalView) | **view** | the [SDL_MetalView](SDL_MetalView) object. |

## Return Value

(void *) Returns a pointer.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMetal](CategoryMetal)

