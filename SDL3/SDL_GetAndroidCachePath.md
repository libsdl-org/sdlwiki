###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAndroidCachePath

Get the path used for caching data for this Android application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
const char * SDL_GetAndroidCachePath(void);
```

## Return Value

(const char *) Returns the path used for caches for this application on
success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

This path is unique to your application, but is public and can be written
to by other applications.

Your cache path is typically: `/data/data/your.app.package/cache/`.

This is a C wrapper over `android.content.Context.getCacheDir()`:

https://developer.android.com/reference/android/content/Context#getCacheDir()

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetAndroidInternalStoragePath](SDL_GetAndroidInternalStoragePath)
- [SDL_GetAndroidExternalStoragePath](SDL_GetAndroidExternalStoragePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

