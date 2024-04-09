###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_ShowCursor

Show the cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_ShowCursor(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
int main(int argc, char *argv[]) {
    /* creates a blank cursor */
    SDL_ShowCursor(SDL_DISABLE);
    /* ... */
    return 0;
}
```

## See Also

* [SDL_CursorVisible](SDL_CursorVisible)
* [SDL_HideCursor](SDL_HideCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse), [CategoryDraft](CategoryDraft)


