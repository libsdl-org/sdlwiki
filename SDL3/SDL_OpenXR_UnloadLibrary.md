# SDL_OpenXR_UnloadLibrary

Unload the OpenXR loader previously loaded by [SDL_OpenXR_LoadLibrary](SDL_OpenXR_LoadLibrary).

## Header File

Defined in [<SDL3/SDL_openxr.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_openxr.h)

## Syntax

```c
void SDL_OpenXR_UnloadLibrary(void);
```

## Remarks

SDL keeps a reference count of the OpenXR loader, calling this function
will decrement that count. Once the reference count reaches zero, the
library is unloaded.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryOpenxr](CategoryOpenxr)

