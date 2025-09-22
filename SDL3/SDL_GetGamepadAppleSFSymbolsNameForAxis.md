# SDL_GetGamepadAppleSFSymbolsNameForAxis

Return the sfSymbolsName for a given axis on a gamepad on Apple platforms.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char * SDL_GetGamepadAppleSFSymbolsNameForAxis(SDL_Gamepad *gamepad, SDL_GamepadAxis axis);
```

## Function Parameters

|                                    |             |                         |
| ---------------------------------- | ----------- | ----------------------- |
| [SDL_Gamepad](SDL_Gamepad) *       | **gamepad** | the gamepad to query.   |
| [SDL_GamepadAxis](SDL_GamepadAxis) | **axis**    | an axis on the gamepad. |

## Return Value

(const char *) Returns the sfSymbolsName or NULL if the name can't be
found.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGamepadAppleSFSymbolsNameForButton](SDL_GetGamepadAppleSFSymbolsNameForButton)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

