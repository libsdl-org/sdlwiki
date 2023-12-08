###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_AndroidGetExternalStorageState

Get the current state of external storage.

## Syntax

```c
int SDL_AndroidGetExternalStorageState(Uint32 *state);

```

## Function Parameters

|               |                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------- |
| **state**     | filled with the current state of external storage. 0 if external storage is currently unavailable. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The current state of external storage, a bitmask of these values:
[`SDL_ANDROID_EXTERNAL_STORAGE_READ`](SDL_ANDROID_EXTERNAL_STORAGE_READ),
[`SDL_ANDROID_EXTERNAL_STORAGE_WRITE`](SDL_ANDROID_EXTERNAL_STORAGE_WRITE).

If external storage is currently unavailable, this will return 0.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AndroidGetExternalStoragePath](SDL_AndroidGetExternalStoragePath.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySystem](CategorySystem.md), [CategoryDraft](CategoryDraft.md), [CategoryAndroid](CategoryAndroid.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
