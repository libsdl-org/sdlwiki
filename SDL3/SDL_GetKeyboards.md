###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetKeyboards

Get a list of currently connected keyboards.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
const SDL_KeyboardID * SDL_GetKeyboards(int *count);
```

## Function Parameters

|       |           |                                                                         |
| ----- | --------- | ----------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of keyboards returned, may be NULL. |

## Return Value

(const [SDL_KeyboardID](SDL_KeyboardID) *) Returns a 0 terminated array of
keyboards instance IDs or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Note that this will include any device or virtual driver that includes
keyboard functionality, including some mice, KVM switches, motherboard
power buttons, etc. You should wait for input from a device before you
consider it actively in use.

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeyboardNameForID](SDL_GetKeyboardNameForID)
- [SDL_HasKeyboard](SDL_HasKeyboard)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

