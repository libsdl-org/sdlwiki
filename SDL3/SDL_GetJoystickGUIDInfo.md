###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickGUIDInfo

Get the device information encoded in a [SDL_JoystickGUID](SDL_JoystickGUID) structure 

## Syntax

```c
void SDL_GetJoystickGUIDInfo(SDL_JoystickGUID guid, Uint16 *vendor, Uint16 *product, Uint16 *version, Uint16 *crc16);

```

## Function Parameters

|                 |                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| **guid**        | the [SDL_JoystickGUID](SDL_JoystickGUID) you wish to get info about                                                |
| **vendor**      | A pointer filled in with the device VID, or 0 if not available                                                     |
| **product**     | A pointer filled in with the device PID, or 0 if not available                                                     |
| **version**     | A pointer filled in with the device version, or 0 if not available                                                 |
| **crc16**       | A pointer filled in with a CRC used to distinguish different products with the same VID/PID, or 0 if not available |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickInstanceGUID](SDL_GetJoystickInstanceGUID)

----
[CategoryAPI](CategoryAPI)

