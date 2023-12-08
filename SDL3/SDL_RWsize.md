###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_RWsize

Use this function to get the size of the data stream in an [SDL_RWops](SDL_RWops.md).

## Syntax

```c
Sint64 SDL_RWsize(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                    |
| --------------- | ------------------------------------------------------------------ |
| **context**     | the [SDL_RWops](SDL_RWops.md) to get the size of the data stream from |

## Return Value

Returns the size of the data stream in the [SDL_RWops](SDL_RWops.md) on
success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryIO](CategoryIO.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
