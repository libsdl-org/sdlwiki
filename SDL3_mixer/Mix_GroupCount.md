###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GroupCount

Returns the number of channels in a group.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_GroupCount(int tag);
```

## Function Parameters

|     |         |                                                          |
| --- | ------- | -------------------------------------------------------- |
| int | **tag** | an arbitrary value, assigned to channels, to search for. |

## Return Value

(int) Returns the number of channels assigned the specified tag.

## Remarks

If tag is -1, this will return the total number of channels allocated,
regardless of what their tag might be.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

