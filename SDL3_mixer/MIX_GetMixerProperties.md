###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetMixerProperties

Get the properties associated with a mixer.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
SDL_PropertiesID MIX_GetMixerProperties(MIX_Mixer *mixer);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer** | the mixer to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Remarks

Currently SDL_mixer assigns no properties of its own to a mixer, but this
can be a convenient place to store app-specific data.

A SDL_PropertiesID is created the first time this function is called for a
given mixer.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

