# SDL_GetJoystickGUIDInfo

Get the device information encoded in a [SDL_GUID](SDL_GUID) structure.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
void SDL_GetJoystickGUIDInfo(SDL_GUID guid, Uint16 *vendor, Uint16 *product, Uint16 *version, Uint16 *crc16);
```

## Function Parameters

|                      |             |                                                                                                                     |
| -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------- |
| [SDL_GUID](SDL_GUID) | **guid**    | the [SDL_GUID](SDL_GUID) you wish to get info about.                                                                |
| [Uint16](Uint16) *   | **vendor**  | a pointer filled in with the device VID, or 0 if not available.                                                     |
| [Uint16](Uint16) *   | **product** | a pointer filled in with the device PID, or 0 if not available.                                                     |
| [Uint16](Uint16) *   | **version** | a pointer filled in with the device version, or 0 if not available.                                                 |
| [Uint16](Uint16) *   | **crc16**   | a pointer filled in with a CRC used to distinguish different products with the same VID/PID, or 0 if not available. |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetJoystickGUIDForID](SDL_GetJoystickGUIDForID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryJoystick](CategoryJoystick)

