# SDL_GetJoystickGUIDInfo

Get the device information encoded in a [SDL_JoystickGUID](SDL_JoystickGUID) structure

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
void SDL_GetJoystickGUIDInfo(SDL_JoystickGUID guid, Uint16 *vendor, Uint16 *product, Uint16 *version, Uint16 *crc16);
```

## Function Parameters

|                                      |             |                                                                                                                     |
| ------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------- |
| [SDL_JoystickGUID](SDL_JoystickGUID) | **guid**    | the [SDL_JoystickGUID](SDL_JoystickGUID) you wish to get info about.                                                |
| [Uint16](Uint16) *                   | **vendor**  | A pointer filled in with the device VID, or 0 if not available.                                                     |
| [Uint16](Uint16) *                   | **product** | A pointer filled in with the device PID, or 0 if not available.                                                     |
| [Uint16](Uint16) *                   | **version** | A pointer filled in with the device version, or 0 if not available.                                                 |
| [Uint16](Uint16) *                   | **crc16**   | A pointer filled in with a CRC used to distinguish different products with the same VID/PID, or 0 if not available. |

## Version

This function is available since SDL 2.26.0.

## See Also

- [SDL_JoystickGetDeviceGUID](SDL_JoystickGetDeviceGUID)


## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

