# SDL_GetOpenHarmonyInternalStoragePath

Get the path used for internal storage for this OpenHarmony application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
const char * SDL_GetOpenHarmonyInternalStoragePath(void);
```

## Return Value

(const char *) Returns the path used for internal storage or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This path is unique to your application and cannot be written to by other
applications.

Your internal storage path is typically: `/data/storage/el2/base/files`.

## Version

This function is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

