# SDL_SetScancodeName

Set a human-readable name for a scancode.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
bool SDL_SetScancodeName(SDL_Scancode scancode, const char *name);
```

## Function Parameters

|                              |              |                                                                                                                                                              |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDL_Scancode](SDL_Scancode) | **scancode** | the desired [SDL_Scancode](SDL_Scancode).                                                                                                                    |
| const char *                 | **name**     | the name to use for the scancode, encoded as UTF-8. The string is not copied, so the pointer given to this function must stay valid while SDL is being used. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetScancodeName](SDL_GetScancodeName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

