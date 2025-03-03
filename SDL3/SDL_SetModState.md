# SDL_SetModState

Set the current key modifier state for the keyboard.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
void SDL_SetModState(SDL_Keymod modstate);
```

## Function Parameters

|                          |              |                                                        |
| ------------------------ | ------------ | ------------------------------------------------------ |
| [SDL_Keymod](SDL_Keymod) | **modstate** | the desired [SDL_Keymod](SDL_Keymod) for the keyboard. |

## Remarks

The inverse of [SDL_GetModState](SDL_GetModState)(),
[SDL_SetModState](SDL_SetModState)() allows you to impose modifier key
states on your application. Simply pass your desired modifier states into
`modstate`. This value may be a bitwise, OR'd combination of
[SDL_Keymod](SDL_Keymod) values.

This does not change the keyboard state, only the key modifier flags that
SDL reports.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetModState](SDL_GetModState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

