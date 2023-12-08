###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HookMusicFinished

Set a callback that runs when a music object has stopped playing.

## Syntax

```c
void Mix_HookMusicFinished(void (SDLCALL *music_finished)(void));

```

## Function Parameters

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| **music_finished**     | the callback function to become the new notification mechanism. |

## Remarks

This callback will fire when the currently-playing music has completed, or
when it has been explicitly stopped from a call to
[Mix_HaltMusic](Mix_HaltMusic.md). As such, this callback might fire from an
arbitrary background thread at almost any time; try to limit what you do
here.

It is legal to start a new music object playing in this callback (or
restart the one that just stopped). If the music finished normally, this
can be used to loop the music without a gap in the audio playback.

Do not call SDL_LockAudio() from this callback; you will either be inside
the audio callback, or SDL_mixer will explicitly lock the audio before
calling your callback.

A NULL pointer will disable the callback.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
