###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Point3D

3D coordinates for [MIX_SetTrack3DPosition](MIX_SetTrack3DPosition).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
typedef struct MIX_Point3D
{
    float x;  /**< X coordinate (negative left, positive right). */
    float y;  /**< Y coordinate (negative down, positive up). */
    float z;  /**< Z coordinate (negative forward, positive back). */
} MIX_Point3D;
```

## Remarks

The coordinates use a "right-handed" coordinate system, like OpenGL and
OpenAL.

## Version

This struct is available since SDL_mixer 3.0.0.

## See Also

- [MIX_SetTrack3DPosition](MIX_SetTrack3DPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategorySDLMixer](CategorySDLMixer)

