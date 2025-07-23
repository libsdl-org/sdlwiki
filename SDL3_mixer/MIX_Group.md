###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Group

An opaque object that represents a grouping of tracks.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef struct MIX_Group MIX_Group;
```

## Remarks

SDL_mixer offers callbacks at various stages of the mixing pipeline to
allow apps to view and manipulate data as it is transformed. Sometimes it
is useful to hook in at a point where several tracks--but not all tracks--
have been mixed. For example, when a game is in some options menu, perhaps
adjusting game audio but not UI sounds could be useful.

SDL_mixer allows you to assign several tracks to a group, and receive a
callback when that group has finished mixing, with a buffer of just that
group's mixed audio, before it mixes into the final output.

## Version

This datatype is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySDLMixer](CategorySDLMixer)

