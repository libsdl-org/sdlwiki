###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CloseAnimationStream

Close an animation stream, finishing any encoding.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_CloseAnimationStream(IMG_AnimationStream *stream);
```

## Function Parameters

|                                              |            |                      |
| -------------------------------------------- | ---------- | -------------------- |
| [IMG_AnimationStream](IMG_AnimationStream) * | **stream** | the stream to close. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Calling this function frees the animation stream, and returns the final
status of the encoding process.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationStream](IMG_CreateAnimationStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

