# SDL_GetDeviceFormFactor

Get the form factor of the current device.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
SDL_FormFactor SDL_GetDeviceFormFactor(void);
```

## Return Value

([SDL_FormFactor](SDL_FormFactor)) Returns the best guess for the form
factor of the current device.

## Remarks

This function guesses what the device may be, but may report inaccurate or
outright wrong results. For example, it may report a laptop as a desktop,
or a car device as a phone.

Depending on the usage, there may be different functions better suited for
each purpose. For example, activating touch controls can be done by
detecting the presence of a touchscreen rather than restricting to phones
and tablets.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_FormFactor](SDL_FormFactor)
- [SDL_GetDeviceFormFactorName](SDL_GetDeviceFormFactorName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

