# SDL_Metal_DestroyView

Destroy an existing [SDL_MetalView](SDL_MetalView) object.

## Header File

Defined in [SDL_metal.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_metal.h)

## Syntax

```c
void SDL_Metal_DestroyView(SDL_MetalView view);
```

## Function Parameters

|                                |          |                                            |
| ------------------------------ | -------- | ------------------------------------------ |
| [SDL_MetalView](SDL_MetalView) | **view** | the [SDL_MetalView](SDL_MetalView) object. |

## Remarks

This should be called before [SDL_DestroyWindow](SDL_DestroyWindow), if
[SDL_Metal_CreateView](SDL_Metal_CreateView) was called after
[SDL_CreateWindow](SDL_CreateWindow).

## Version

This function is available since SDL 2.0.12.

## See Also

- [SDL_Metal_CreateView](SDL_Metal_CreateView)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMetal](CategoryMetal)

