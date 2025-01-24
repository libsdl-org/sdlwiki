# SDL_Finger

Data about a single finger in a multitouch event.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
typedef struct SDL_Finger
{
    SDL_FingerID id;  /**< the finger ID */
    float x;  /**< the x-axis location of the touch event, normalized (0...1) */
    float y;  /**< the y-axis location of the touch event, normalized (0...1) */
    float pressure; /**< the quantity of pressure applied, normalized (0...1) */
} SDL_Finger;
```

## Remarks

Each touch event is a collection of fingers that are simultaneously in
contact with the touch device (so a "touch" can be a "multitouch," in
reality), and this struct reports details of the specific fingers.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GetTouchFingers](SDL_GetTouchFingers)






----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryTouch](CategoryTouch)

