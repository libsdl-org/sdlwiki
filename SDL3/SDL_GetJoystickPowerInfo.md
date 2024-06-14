###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickPowerInfo

Get the battery state of a joystick.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
SDL_PowerState SDL_GetJoystickPowerInfo(SDL_Joystick *joystick, int *percent);
```

## Function Parameters

|                                |              |                                                                                                                                                                                       |
| ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Joystick](SDL_Joystick) * | **joystick** | the joystick to query.                                                                                                                                                                |
| int *                          | **percent**  | a pointer filled in with the percentage of battery life left, between 0 and 100, or NULL to ignore. This will be filled in with -1 we can't determine a value or there is no battery. |

## Return Value

([SDL_PowerState](SDL_PowerState)) Returns the current battery state or
[`SDL_POWERSTATE_ERROR`](SDL_POWERSTATE_ERROR) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You should never take a battery status as absolute truth. Batteries
(especially failing batteries) are delicate hardware, and the values
reported here are best estimates based on what that hardware reports. It's
not uncommon for older batteries to lose stored power much faster than it
reports, or completely drain when reporting it has 20 percent left, etc.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

