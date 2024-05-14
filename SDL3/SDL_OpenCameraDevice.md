###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenCameraDevice

Open a video capture device (a "camera").

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
SDL_Camera* SDL_OpenCameraDevice(SDL_CameraDeviceID instance_id, const SDL_CameraSpec *spec);

```

## Function Parameters

|                     |                                                                   |
| ------------------- | ----------------------------------------------------------------- |
| **instance_id**     | the camera device instance ID                                     |
| **spec**            | The desired format for data the device will provide. Can be NULL. |

## Return Value

Returns device, or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

You can open the device with any reasonable spec, and if the hardware can't
directly support it, it will convert data seamlessly to the requested
format. This might incur overhead, including scaling of image data.

If you would rather accept whatever format the device offers, you can pass
a NULL spec here and it will choose one for you (and you can use
[SDL_Surface](SDL_Surface)'s conversion/scaling functions directly if
necessary).

You can call [SDL_GetCameraFormat](SDL_GetCameraFormat)() to get the actual
data format if passing a NULL spec here. You can see the exact specs a
device can support without conversion with
[SDL_GetCameraSupportedSpecs](SDL_GetCameraSupportedSpecs)().

SDL will not attempt to emulate framerate; it will try to set the hardware
to the rate closest to the requested speed, but it won't attempt to limit
or duplicate frames artificially; call
[SDL_GetCameraFormat](SDL_GetCameraFormat)() to see the actual framerate of
the opened the device, and check your timestamps if this is crucial to your
app!

Note that the camera is not usable until the user approves its use! On some
platforms, the operating system will prompt the user to permit access to
the camera, and they can choose Yes or No at that point. Until they do, the
camera will not be usable. The app should either wait for an
[SDL_EVENT_CAMERA_DEVICE_APPROVED](SDL_EVENT_CAMERA_DEVICE_APPROVED) (or
[SDL_EVENT_CAMERA_DEVICE_DENIED](SDL_EVENT_CAMERA_DEVICE_DENIED)) event, or
poll [SDL_IsCameraApproved](SDL_IsCameraApproved)() occasionally until it
returns non-zero. On platforms that don't require explicit user approval
(and perhaps in places where the user previously permitted access), the
approval event might come immediately, but it might come seconds, minutes,
or hours later!

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCameraDevices](SDL_GetCameraDevices)
- [SDL_GetCameraFormat](SDL_GetCameraFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

