###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_ChannelFinished

Set a callback that runs when a channel has finished playing.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void Mix_ChannelFinished(Mix_ChannelFinishedCallback channel_finished);
```

## Function Parameters

|                                                            |                      |                                                                 |
| ---------------------------------------------------------- | -------------------- | --------------------------------------------------------------- |
| [Mix_ChannelFinishedCallback](Mix_ChannelFinishedCallback) | **channel_finished** | the callback function to become the new notification mechanism. |

## Remarks

The callback may be called from the mixer's audio callback or it could be
called as a result of [Mix_HaltChannel](Mix_HaltChannel)(), etc.

The callback has a single parameter, `channel`, which says what mixer
channel has just stopped.

A NULL pointer will disable the callback.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

