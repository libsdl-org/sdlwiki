###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDefaultCursor

Get the default cursor.

## Syntax

```c
SDL_Cursor* SDL_GetDefaultCursor(void);

```

## Return Value

Returns the default cursor on success or NULL on failure.

## Remarks

You do not have to call [SDL_FreeCursor](SDL_FreeCursor.md)() on the return
value, but it is safe to do so.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateSystemCursor](SDL_CreateSystemCursor.md)

----
[CategoryAPI](CategoryAPI.md)
