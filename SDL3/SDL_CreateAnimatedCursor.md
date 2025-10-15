# SDL_CreateAnimatedCursor

Create an animated color cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_Cursor* SDL_CreateAnimatedCursor(SDL_CursorFrameInfo *frames,
                                     int frame_count,
                                     int hot_x,
                                     int hot_y);
```

## Function Parameters

|                                              |                 |                                                    |
| -------------------------------------------- | --------------- | -------------------------------------------------- |
| [SDL_CursorFrameInfo](SDL_CursorFrameInfo) * | **frames**      | an array of cursor images composing the animation. |
| int                                          | **frame_count** | the number of frames in the sequence.              |
| int                                          | **hot_x**       | the x position of the cursor hot spot.             |
| int                                          | **hot_y**       | the y position of the cursor hot spot.             |

## Return Value

([SDL_Cursor](SDL_Cursor) *) Returns the new cursor on success or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Animated cursors are composed of a sequential array of frames, specified as
surfaces and durations in an array of
[SDL_CursorFrameInfo](SDL_CursorFrameInfo) structs. The hot spot
coordinates are universal to all frames, and all frames must have the same
dimensions.

Frame durations are specified in milliseconds. A duration of 0 implies an
infinite frame time, and the animation will stop on that frame. To create a
one-shot animation, set the duration of the last frame in the sequence to
0.

If this function is passed surfaces with alternate representations added
with [SDL_AddSurfaceAlternateImage](SDL_AddSurfaceAlternateImage)(), the
surfaces will be interpreted as the content to be used for 100% display
scale, and the alternate representations will be used for high DPI
situations. For example, if the original surfaces are 32x32, then on a 2x
macOS display or 200% display scale on Windows, a 64x64 version of the
image will be used, if available. If a matching version of the image isn't
available, the closest larger size image will be downscaled to the
appropriate size and be used instead, if available. Otherwise, the closest
smaller image will be upscaled and be used instead.

If the underlying platform does not support animated cursors, this function
will fall back to creating a static color cursor using the first frame in
the sequence.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_AddSurfaceAlternateImage](SDL_AddSurfaceAlternateImage)
- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)
- [SDL_DestroyCursor](SDL_DestroyCursor)
- [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

