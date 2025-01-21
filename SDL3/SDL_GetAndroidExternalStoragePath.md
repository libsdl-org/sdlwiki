###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAndroidExternalStorageState](SDL_GetAndroidExternalStorageState)
- [SDL_GetAndroidInternalStoragePath](SDL_GetAndroidInternalStoragePath)
- [SDL_GetAndroidCachePath](SDL_GetAndroidCachePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

