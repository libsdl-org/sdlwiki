###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetRenderDriver

Use this function to get the name of a built in 2D rendering driver.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
const char * SDL_GetRenderDriver(int index);
```

## Function Parameters

|     |           |                                                                                                                         |
| --- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| int | **index** | the index of the rendering driver; the value ranges from 0 to [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)() - 1. |

## Return Value

(const char *) Returns the name of the rendering driver at the requested
index, or NULL if an invalid index was specified.

## Remarks

The list of rendering drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "opengl",
"direct3d12" or "metal". These never have Unicode characters, and are not
meant to be proper names.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## Code examples

```c
// Log drivers that are available, in the order of priority SDL chooses them.
// Useful for e.g. debugging which ones a particular build of SDL contains.
SDL_Log("Available renderer drivers:");
for (int i = 0; i < SDL_GetNumRenderDrivers(); i++) {
    SDL_Log("%d. %s", i + 1, SDL_GetRenderDriver(i));
}
```

## See Also

- [SDL_GetNumRenderDrivers](SDL_GetNumRenderDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

