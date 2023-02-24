###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetJoystickGUIDString

Get an ASCII string representation for a given [SDL_JoystickGUID](SDL_JoystickGUID).

## Syntax

```c
int SDL_GetJoystickGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);

```

## Function Parameters

|                 |                                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **guid**        | the [SDL_JoystickGUID](SDL_JoystickGUID) you wish to convert to string |
| **pszGUID**     | buffer in which to write the ASCII string                              |
| **cbGUID**      | the size of pszGUID                                                    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You should supply at least 33 bytes for pszGUID.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetJoystickInstanceGUID](SDL_GetJoystickInstanceGUID)
* [SDL_GetJoystickGUID](SDL_GetJoystickGUID)
* [SDL_GetJoystickGUIDFromString](SDL_GetJoystickGUIDFromString)

----
[CategoryAPI](CategoryAPI)

