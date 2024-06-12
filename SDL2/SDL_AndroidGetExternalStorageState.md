###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidGetExternalStorageState

Get the current state of external storage.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
int SDL_AndroidGetExternalStorageState(void);
```

## Return Value

(int) Returns the current state of external storage on success or 0 on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The current state of external storage, a bitmask of these values:
[`SDL_ANDROID_EXTERNAL_STORAGE_READ`](SDL_ANDROID_EXTERNAL_STORAGE_READ),
[`SDL_ANDROID_EXTERNAL_STORAGE_WRITE`](SDL_ANDROID_EXTERNAL_STORAGE_WRITE).

If external storage is currently unavailable, this will return 0.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AndroidGetExternalStoragePath](SDL_AndroidGetExternalStoragePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

