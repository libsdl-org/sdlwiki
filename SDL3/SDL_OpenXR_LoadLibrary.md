# SDL_OpenXR_LoadLibrary

Dynamically load the OpenXR loader.

## Header File

Defined in [<SDL3/SDL_openxr.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_openxr.h)

## Syntax

```c
bool SDL_OpenXR_LoadLibrary(void);
```

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This can be called at any time.

SDL keeps a reference count of the OpenXR loader, calling this function
multiple times will increment that count, rather than loading the library
multiple times.

If not called, this will be implicitly called when creating a GPU device
with OpenXR.

This function will use the platform default OpenXR loader name, unless the
[`SDL_HINT_OPENXR_LIBRARY`](SDL_HINT_OPENXR_LIBRARY) hint is set.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_HINT_OPENXR_LIBRARY](SDL_HINT_OPENXR_LIBRARY)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryOpenxr](CategoryOpenxr)

