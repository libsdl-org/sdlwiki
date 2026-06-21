# SDL_GetDeviceFormFactorName

Get a short name for the current device.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
const char* SDL_GetDeviceFormFactorName(SDL_FormFactor form_factor);
```

## Function Parameters

|                                  |                 |                           |
| -------------------------------- | --------------- | ------------------------- |
| [SDL_FormFactor](SDL_FormFactor) | **form_factor** | the form factor to query. |

## Return Value

(const char *) Returns a human-readable name for the given form factor, or
"[SDL_FORMFACTOR_UNKNOWN](SDL_FORMFACTOR_UNKNOWN)" if the form factor isn't
recognized.

## Remarks

The name will be in English.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_FormFactor](SDL_FormFactor)
- [SDL_GetDeviceFormFactor](SDL_GetDeviceFormFactor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

