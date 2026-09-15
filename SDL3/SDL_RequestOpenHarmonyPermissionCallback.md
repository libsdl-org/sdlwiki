# SDL_RequestOpenHarmonyPermissionCallback

Callback that presents [SDL_RequestOpenHarmonyPermission](SDL_RequestOpenHarmonyPermission)() results.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef void (SDLCALL *SDL_RequestOpenHarmonyPermissionCallback)(void *userdata, const char *permission, bool granted);
```

## Function Parameters

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| **userdata**   | an app-controlled pointer that is passed to the callback.    |
| **permission** | the OpenHarmony-specific permission name that was requested. |
| **granted**    | true if permission is granted, false if denied.              |

## Version

This datatype is available since SDL 3.6.0.

## See Also

- [SDL_RequestOpenHarmonyPermission](SDL_RequestOpenHarmonyPermission)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySystem](CategorySystem)

