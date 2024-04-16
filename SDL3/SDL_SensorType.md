###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SensorType

The different sensors defined by SDL.

## Header File

Defined in [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_sensor.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_SensorType
{
    SDL_SENSOR_INVALID = -1,    /**< Returned for an invalid sensor */
    SDL_SENSOR_UNKNOWN,         /**< Unknown sensor type */
    SDL_SENSOR_ACCEL,           /**< Accelerometer */
    SDL_SENSOR_GYRO,            /**< Gyroscope */
    SDL_SENSOR_ACCEL_L,         /**< Accelerometer for left Joy-Con controller and Wii nunchuk */
    SDL_SENSOR_GYRO_L,          /**< Gyroscope for left Joy-Con controller */
    SDL_SENSOR_ACCEL_R,         /**< Accelerometer for right Joy-Con controller */
    SDL_SENSOR_GYRO_R           /**< Gyroscope for right Joy-Con controller */
} SDL_SensorType;
```

## Remarks

Additional sensors may be available, using platform dependent semantics.

Hare are the additional Android sensors:
https://developer.android.com/reference/android/hardware/SensorEvent.html#values

Accelerometer sensor notes:

The accelerometer returns the current acceleration in SI meters per second
squared. This measurement includes the force of gravity, so a device at
rest will have an value of [SDL_STANDARD_GRAVITY](SDL_STANDARD_GRAVITY)
away from the center of the earth, which is a positive Y value.

- `values[0]`: Acceleration on the x axis
- `values[1]`: Acceleration on the y axis
- `values[2]`: Acceleration on the z axis

For phones and tablets held in natural orientation and game controllers
held in front of you, the axes are defined as follows:

- -X ... +X : left ... right
- -Y ... +Y : bottom ... top
- -Z ... +Z : farther ... closer

The accelerometer axis data is not changed when the device is rotated.

Gyroscope sensor notes:

The gyroscope returns the current rate of rotation in radians per second.
The rotation is positive in the counter-clockwise direction. That is, an
observer looking from a positive location on one of the axes would see
positive rotation on that axis when it appeared to be rotating
counter-clockwise.

- `values[0]`: Angular speed around the x axis (pitch)
- `values[1]`: Angular speed around the y axis (yaw)
- `values[2]`: Angular speed around the z axis (roll)

For phones and tablets held in natural orientation and game controllers
held in front of you, the axes are defined as follows:

- -X ... +X : left ... right
- -Y ... +Y : bottom ... top
- -Z ... +Z : farther ... closer

The gyroscope axis data is not changed when the device is rotated.

## Version

This enum is available since SDL 3.0.0.

## See Also

* [SDL_GetCurrentDisplayOrientation](SDL_GetCurrentDisplayOrientation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

