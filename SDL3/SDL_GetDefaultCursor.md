###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetDefaultCursor

Get the default cursor.

## Syntax

```c
SDL_Cursor* SDL_GetDefaultCursor(void);

```

## Return Value

Returns the default cursor on success or NULL on failure.

## Remarks

You do not have to call [SDL_DestroyCursor](SDL_DestroyCursor)() on the
return value, but it is safe to do so.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateSystemCursor](SDL_CreateSystemCursor)

----
[CategoryAPI](CategoryAPI), [CategoryMouse](CategoryMouse), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


