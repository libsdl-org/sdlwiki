###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Metal_CreateView

Create a CAMetalLayer-backed NSView/UIView and attach it to the specified window.

## Header File

Defined in [<SDL3/SDL_metal.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_metal.h)

## Syntax

```c
SDL_MetalView SDL_Metal_CreateView(SDL_Window * window);
```

## Function Parameters

|                            |            |             |
| -------------------------- | ---------- | ----------- |
| [SDL_Window](SDL_Window) * | **window** | the window. |

## Return Value

([SDL_MetalView](SDL_MetalView)) Returns handle NSView or UIView.

## Remarks

On macOS, this does *not* associate a MTLDevice with the CAMetalLayer on
its own. It is up to user code to do that.

The returned handle can be casted directly to a NSView or UIView. To access
the backing CAMetalLayer, call [SDL_Metal_GetLayer](SDL_Metal_GetLayer)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_Metal_DestroyView](SDL_Metal_DestroyView)
- [SDL_Metal_GetLayer](SDL_Metal_GetLayer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMetal](CategoryMetal)

