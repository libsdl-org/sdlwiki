###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_CreateSystemCursor

Create a system cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_Cursor* SDL_CreateSystemCursor(SDL_SystemCursor id);

```

## Function Parameters

|            |                                                    |
| ---------- | -------------------------------------------------- |
| **id**     | an [SDL_SystemCursor](SDL_SystemCursor) enum value |

## Return Value

Returns a cursor on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_Cursor* cursor;
cursor = SDL_CreateSystemCursor(SDL_SYSTEM_CURSOR_HAND);
SDL_SetCursor(cursor);
```

## Related Functions

* [SDL_DestroyCursor](SDL_DestroyCursor)

----
[CategoryAPI](CategoryAPI), [CategoryMouse](CategoryMouse), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


