###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_AndroidGetExternalStoragePath

Get the path used for external storage for this application.

## Syntax

```c
const char * SDL_AndroidGetExternalStoragePath(void);

```

## Return Value

Returns the path used for external storage for this application on success
or NULL on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

This path is unique to your application, but is public and can be written
to by other applications.

Your external storage path is typically:
`/storage/sdcard0/Android/data/your.app.package/files`.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AndroidGetExternalStorageState](SDL_AndroidGetExternalStorageState.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySystem](CategorySystem.md), [CategoryDraft](CategoryDraft.md), [CategoryAndroid](CategoryAndroid.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
