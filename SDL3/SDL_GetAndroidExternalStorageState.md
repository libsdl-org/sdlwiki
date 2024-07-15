###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAndroidExternalStorageState

Get the current state of external storage for this Android application.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_GetAndroidExternalStorageState(Uint32 *state);
```

## Function Parameters

|          |           |                                                                                                    |
| -------- | --------- | -------------------------------------------------------------------------------------------------- |
| Uint32 * | **state** | filled with the current state of external storage. 0 if external storage is currently unavailable. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The current state of external storage, a bitmask of these values:
[`SDL_ANDROID_EXTERNAL_STORAGE_READ`](SDL_ANDROID_EXTERNAL_STORAGE_READ),
[`SDL_ANDROID_EXTERNAL_STORAGE_WRITE`](SDL_ANDROID_EXTERNAL_STORAGE_WRITE).

If external storage is currently unavailable, this will return 0.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAndroidExternalStoragePath](SDL_GetAndroidExternalStoragePath)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

