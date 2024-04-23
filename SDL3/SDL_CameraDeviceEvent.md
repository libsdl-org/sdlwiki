###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CameraDeviceEvent

Camera device event structure (event.cdevice.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_CameraDeviceEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_CAMERA_DEVICE_ADDED, ::SDL_EVENT_CAMERA_DEVICE_REMOVED, ::SDL_EVENT_CAMERA_DEVICE_APPROVED, ::SDL_EVENT_CAMERA_DEVICE_DENIED */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_CameraDeviceID which;       /**< SDL_CameraDeviceID for the device being added or removed or changing */
} SDL_CameraDeviceEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

