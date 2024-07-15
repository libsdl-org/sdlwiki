###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAndroidExternalStoragePath

Get the path used for external storage for this Android application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
const char * SDL_GetAndroidExternalStoragePath(void);
```

## Return Value

(const char *) Returns the path used for external storage for this
application on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This path is unique to your application, but is public and can be written
to by other applications.

Your external storage path is typically:
`/storage/sdcard0/Android/data/your.app.package/files`.

This is a C wrapper over `android.content.Context.getExternalFilesDir()`:

https://developer.android.com/reference/android/content/Context#getExternalFilesDir()

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAndroidExternalStorageState](SDL_GetAndroidExternalStorageState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

