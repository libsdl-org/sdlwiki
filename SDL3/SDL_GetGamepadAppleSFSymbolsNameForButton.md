###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadAppleSFSymbolsNameForButton

Return the sfSymbolsName for a given button on a gamepad on Apple platforms.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
const char* SDL_GetGamepadAppleSFSymbolsNameForButton(SDL_Gamepad *gamepad, SDL_GamepadButton button);
```

## Function Parameters

|                                        |             |                         |
| -------------------------------------- | ----------- | ----------------------- |
| [SDL_Gamepad](SDL_Gamepad) *           | **gamepad** | the gamepad to query    |
| [SDL_GamepadButton](SDL_GamepadButton) | **button**  | a button on the gamepad |

## Return Value

(const char *) Returns the sfSymbolsName or NULL if the name can't be found

## Remarks

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadAppleSFSymbolsNameForAxis](SDL_GetGamepadAppleSFSymbolsNameForAxis)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

