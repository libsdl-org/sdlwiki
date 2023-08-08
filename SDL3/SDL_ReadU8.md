###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_ReadU8

Use this function to read a byte from an [SDL_RWops](SDL_RWops).

## Syntax

```c
SDL_bool SDL_ReadU8(SDL_RWops *src, Uint8 *value);

```

## Function Parameters

|               |                                         |
| ------------- | --------------------------------------- |
| **src**       | the [SDL_RWops](SDL_RWops) to read from |
| **value**     | a pointer filled in with the data read  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) on success or [SDL_FALSE](SDL_FALSE) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryIO](CategoryIO), [CategoryDraft](CategoryDraft)


