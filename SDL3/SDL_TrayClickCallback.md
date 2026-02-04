# SDL_TrayClickCallback

A callback that is invoked when the tray icon is clicked.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
typedef bool (SDLCALL *SDL_TrayClickCallback)(void *userdata, SDL_Tray *tray);
```

## Function Parameters

|              |                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------- |
| **userdata** | an optional pointer to pass extra data to the callback when it will be invoked. May be NULL. |
| **tray**     | the tray that was clicked.                                                                   |

## Return Value

Returns true to show the tray menu after the callback returns, false to
skip showing the menu. This return value is only used for left and right
click callbacks; other mouse events ignore the return value.

## Version

This datatype is available since SDL 3.6.0.

## See Also

- [SDL_CreateTrayWithProperties](SDL_CreateTrayWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTray](CategoryTray)

