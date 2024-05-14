###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_VirtualJoystickSensorDesc

The structure that describes a virtual joystick sensor.

## Header File

Defined in [<SDL3/SDL_joystick.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_joystick.h)

## Syntax

```c
typedef struct SDL_VirtualJoystickSensorDesc
{
    SDL_SensorType type;    /**< the type of this sensor */
    float rate;             /**< the update frequency of this sensor, may be 0.0f */
} SDL_VirtualJoystickSensorDesc;
```

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_VirtualJoystickDesc](SDL_VirtualJoystickDesc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryJoystick](CategoryJoystick)

