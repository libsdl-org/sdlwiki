###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetAndroidExternalStorageState

Get the current state of external storage for this Android application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
Uint32 SDL_GetAndroidExternalStorageState(void);
```

## Return Value

(Uint32) Returns the current state of external storage, or 0 if external
storage is currently unavailable.

## Remarks

The current state of external storage, a bitmask of these values:
[`SDL_ANDROID_EXTERNAL_STORAGE_READ`](SDL_ANDROID_EXTERNAL_STORAGE_READ),
[`SDL_ANDROID_EXTERNAL_STORAGE_WRITE`](SDL_ANDROID_EXTERNAL_STORAGE_WRITE).

If external storage is currently unavailable, this will return 0.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetAndroidExternalStoragePath](SDL_GetAndroidExternalStoragePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

