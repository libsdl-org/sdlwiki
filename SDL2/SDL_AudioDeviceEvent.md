###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_AudioDeviceEvent

Audio device event structure (event.adevice.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_AudioDeviceEvent
{
    Uint32 type;        /**< ::SDL_AUDIODEVICEADDED, or ::SDL_AUDIODEVICEREMOVED */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 which;       /**< The audio device index for the ADDED event (valid until next SDL_GetNumAudioDevices() call), SDL_AudioDeviceID for the REMOVED event */
    Uint8 iscapture;    /**< zero if an output device, non-zero if a capture device. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_AudioDeviceEvent;
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_AUDIODEVICEADDED, or SDL_AUDIODEVICEREMOVED
|-
|Uint32
|'''timestamp'''
|the timestamp of the event
|-
|Uint32
|'''which'''
|the audio device index for the SDL_AUDIODEVICEADDED event (valid until next [[SDL_GetNumAudioDevices]]() call), SDL_AudioDeviceID for the SDL_AUDIODEVICEREMOVED event
|-
|Uint8
|'''iscapture'''
|zero if an audio output device, non-zero if an audio capture device
|}

## Related Enumerations

:[[SDL_EventType]]

## Related Structures

:[[SDL_Event]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents), [CategoryDraft](CategoryDraft)


