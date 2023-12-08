###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetHintBoolean

Get the boolean value of a hint variable.

## Syntax

```c
SDL_bool SDL_GetHintBoolean(const char *name, SDL_bool default_value);

```

## Function Parameters

|                       |                                                    |
| --------------------- | -------------------------------------------------- |
| **name**              | the name of the hint to get the boolean value from |
| **default_value**     | the value to return if the hint does not exist     |

## Return Value

Returns the boolean value of a hint or the provided default value if the
hint does not exist.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetHint](SDL_GetHint.md)
* [SDL_SetHint](SDL_SetHint.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
