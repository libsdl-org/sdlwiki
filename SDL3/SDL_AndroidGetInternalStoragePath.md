###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_AndroidGetInternalStoragePath

Get the path used for internal storage for this application.

## Syntax

```c
const char * SDL_AndroidGetInternalStoragePath(void);

```

## Return Value

Returns the path used for internal storage or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This path is unique to your application and cannot be written to by other
applications.

Your internal storage path is typically:
`/data/data/your.app.package/files`.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AndroidGetExternalStorageState](SDL_AndroidGetExternalStorageState.md)

----
[CategoryAPI](CategoryAPI.md), [CategorySystem](CategorySystem.md), [CategoryDraft](CategoryDraft.md), [CategoryAndroid](CategoryAndroid.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
