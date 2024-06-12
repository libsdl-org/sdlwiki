###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_Chunk

The internal format for an audio chunk

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef struct Mix_Chunk {
    int allocated;
    Uint8 *abuf;
    Uint32 alen;
    Uint8 volume;       /* Per-sample volume, 0-128 */
} Mix_Chunk;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

