###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationEncoderWithProperties

Create an animation encoder with the specified properties.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationEncoder * IMG_CreateAnimationEncoderWithProperties(SDL_PropertiesID props);


#define IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING                "SDL_image.animation_encoder.create.filename"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER               "SDL_image.animation_encoder.create.iostream"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN     "SDL_image.animation_encoder.create.iostream.autoclose"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_TYPE_STRING                    "SDL_image.animation_encoder.create.type"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_QUALITY_NUMBER                 "SDL_image.animation_encoder.create.quality"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_NUMERATOR_NUMBER      "SDL_image.animation_encoder.create.timebase.numerator"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER    "SDL_image.animation_encoder.create.timebase.denominator"

#define IMG_PROP_ANIMATION_ENCODER_CREATE_AVIF_MAX_THREADS_NUMBER        "SDL_image.animation_encoder.create.avif.max_threads"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_AVIF_KEYFRAME_INTERVAL_NUMBER  "SDL_image.animation_encoder.create.avif.keyframe_interval"
#define IMG_PROP_ANIMATION_ENCODER_CREATE_GIF_USE_LUT_BOOLEAN            "SDL_image.animation_encoder.create.gif.use_lut"
```

## Function Parameters

|                  |           |                                          |
| ---------------- | --------- | ---------------------------------------- |
| SDL_PropertiesID | **props** | the properties of the animation encoder. |

## Return Value

([IMG_AnimationEncoder](IMG_AnimationEncoder) *) Returns a new
[IMG_AnimationEncoder](IMG_AnimationEncoder), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

These animation types are currently supported:

- ANI
- APNG
- AVIFS
- GIF
- WEBP

These are the supported properties:

- [`IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING):
  the file to save, if an SDL_IOStream isn't being used. This is required
  if
  [`IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER`](IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER)
  isn't set.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER`](IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_POINTER):
  an SDL_IOStream that will be used to save the stream. This should not be
  closed until the animation encoder is closed. This is required if
  [`IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING)
  isn't set.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN`](IMG_PROP_ANIMATION_ENCODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN):
  true if closing the animation encoder should also close the associated
  SDL_IOStream.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_TYPE_STRING`](IMG_PROP_ANIMATION_ENCODER_CREATE_TYPE_STRING):
  the output file type, e.g. "webp", defaults to the file extension if
  [`IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_ENCODER_CREATE_FILENAME_STRING)
  is set.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_QUALITY_NUMBER`](IMG_PROP_ANIMATION_ENCODER_CREATE_QUALITY_NUMBER):
  the compression quality, in the range of 0 to 100. The higher the number,
  the higher the quality and file size. This defaults to a balanced value
  for compression and quality.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_NUMERATOR_NUMBER`](IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_NUMERATOR_NUMBER):
  the numerator of the fraction used to multiply the pts to convert it to
  seconds. This defaults to 1.
- [`IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER`](IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER):
  the denominator of the fraction used to multiply the pts to convert it to
  seconds. This defaults to 1000.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationEncoder](IMG_CreateAnimationEncoder)
- [IMG_CreateAnimationEncoder_IO](IMG_CreateAnimationEncoder_IO)
- [IMG_AddAnimationEncoderFrame](IMG_AddAnimationEncoderFrame)
- [IMG_CloseAnimationEncoder](IMG_CloseAnimationEncoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

