###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_GetScancodeFromKey

Get the scancode corresponding to the given key code according to the current keyboard layout.

## Syntax

```c
SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key);

```

## Function Parameters

|             |                                                 |
| ----------- | ----------------------------------------------- |
| **key**     | the desired [SDL_Keycode](SDL_Keycode) to query |

## Return Value

Returns the [SDL_Scancode](SDL_Scancode) that corresponds to the given
[SDL_Keycode](SDL_Keycode).

## Remarks

See [SDL_Scancode](SDL_Scancode) for details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetKeyFromScancode](SDL_GetKeyFromScancode)
* [SDL_GetScancodeName](SDL_GetScancodeName)

----
[CategoryAPI](CategoryAPI), [CategoryKeyboard](CategoryKeyboard), [CategoryDraft](CategoryDraft)


