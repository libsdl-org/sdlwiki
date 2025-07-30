# SDL_AudioDeviceEvent

Audio device event structure (event.adevice.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_AudioDeviceEvent
{
    SDL_EventType type; /**< SDL_EVENT_AUDIO_DEVICE_ADDED, or SDL_EVENT_AUDIO_DEVICE_REMOVED, or SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_AudioDeviceID which;       /**< SDL_AudioDeviceID for the device being added or removed or changing */
    bool recording; /**< false if a playback device, true if a recording device. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_AudioDeviceEvent;
```

## Remarks

Note that SDL will send a
[SDL_EVENT_AUDIO_DEVICE_ADDED](SDL_EVENT_AUDIO_DEVICE_ADDED) event for
every device it discovers during initialization. After that, this event
will only arrive when a device is hotplugged during the program's run.

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

