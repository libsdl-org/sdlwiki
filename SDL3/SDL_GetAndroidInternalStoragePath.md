###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAndroidInternalStoragePath

Get the path used for internal storage for this Android application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
const char* SDL_GetAndroidInternalStoragePath(void);
```

## Return Value

(const char *) Returns the path used for internal storage or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This path is unique to your application and cannot be written to by other
applications.

Your internal storage path is typically:
`/data/data/your.app.package/files`.

This is a C wrapper over `android.content.Context.getFilesDir()`:

https://developer.android.com/reference/android/content/Context#getFilesDir()

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAndroidExternalStorageState](SDL_GetAndroidExternalStorageState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

