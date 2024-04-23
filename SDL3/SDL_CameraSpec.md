###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CameraSpec

The details of an output format for a camera device.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
typedef struct SDL_CameraSpec
{
    SDL_PixelFormatEnum format; /**< Frame format */
    int width;                  /**< Frame width */
    int height;                 /**< Frame height */
    int interval_numerator;     /**< Frame rate numerator ((dom / num) == fps, (num / dom) == duration) */
    int interval_denominator;   /**< Frame rate demoninator ((dom / num) == fps, (num / dom) == duration) */
} SDL_CameraSpec;
```

## Remarks

Cameras often support multiple formats; each one will be encapsulated in
this struct.

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_GetCameraDeviceSupportedFormats](SDL_GetCameraDeviceSupportedFormats)
* [SDL_GetCameraFormat](SDL_GetCameraFormat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

