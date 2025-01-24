# SDL_HINT_JOYSTICK_ENHANCED_REPORTS

A variable controlling whether enhanced reports should be used for controllers when using the HIDAPI driver.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ENHANCED_REPORTS "SDL_JOYSTICK_ENHANCED_REPORTS"
```

## Remarks

Enhanced reports allow rumble and effects on Bluetooth PlayStation
controllers and gyro on Nintendo Switch controllers, but break Windows
DirectInput for other applications that don't use SDL.

Once enhanced reports are enabled, they can't be disabled on PlayStation
controllers without power cycling the controller.

The variable can be set to the following values:

- "0": enhanced reports are not enabled.
- "1": enhanced reports are enabled. (default)
- "auto": enhanced features are advertised to the application, but SDL
  doesn't change the controller report mode unless the application uses
  them.

This hint can be enabled anytime.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

