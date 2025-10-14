# SDL_GetPenDeviceType

Get the device type of the given pen.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
SDL_PenDeviceType SDL_GetPenDeviceType(SDL_PenID instance_id);
```

## Function Parameters

|                        |                 |                      |
| ---------------------- | --------------- | -------------------- |
| [SDL_PenID](SDL_PenID) | **instance_id** | the pen instance ID. |

## Return Value

([SDL_PenDeviceType](SDL_PenDeviceType)) Returns the device type of the
given pen, or [SDL_PEN_DEVICE_TYPE_INVALID](SDL_PEN_DEVICE_TYPE_INVALID) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Many platforms do not supply this information, so an app must always be
prepared to get an
[SDL_PEN_DEVICE_TYPE_UNKNOWN](SDL_PEN_DEVICE_TYPE_UNKNOWN) result.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

