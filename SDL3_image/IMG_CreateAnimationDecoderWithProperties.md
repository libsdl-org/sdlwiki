###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationDecoderWithProperties

Create an animation decoder with the specified properties.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationDecoder * IMG_CreateAnimationDecoderWithProperties(SDL_PropertiesID props);


#define IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING                "SDL_image.animation_decoder.create.filename"
#define IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER               "SDL_image.animation_decoder.create.iostream"
#define IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN     "SDL_image.animation_decoder.create.iostream.autoclose"
#define IMG_PROP_ANIMATION_DECODER_CREATE_TYPE_STRING                    "SDL_image.animation_decoder.create.type"
#define IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_NUMERATOR_NUMBER      "SDL_image.animation_decoder.create.timebase.numerator"
#define IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER    "SDL_image.animation_decoder.create.timebase.denominator"

#define IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_MAX_THREADS_NUMBER        "SDL_image.animation_decoder.create.avif.max_threads"
#define IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_ALLOW_INCREMENTAL_BOOLEAN "SDL_image.animation_decoder.create.avif.allow_incremental"
#define IMG_PROP_ANIMATION_DECODER_CREATE_AVIF_ALLOW_PROGRESSIVE_BOOLEAN "SDL_image.animation_decoder.create.avif.allow_progressive"
#define IMG_PROP_ANIMATION_DECODER_CREATE_GIF_TRANSPARENT_COLOR_INDEX_NUMBER "SDL_image.animation_encoder.create.gif.transparent_color_index"
#define IMG_PROP_ANIMATION_DECODER_CREATE_GIF_NUM_COLORS_NUMBER          "SDL_image.animation_encoder.create.gif.num_colors"
```

## Function Parameters

|                  |           |                                          |
| ---------------- | --------- | ---------------------------------------- |
| SDL_PropertiesID | **props** | the properties of the animation decoder. |

## Return Value

([IMG_AnimationDecoder](IMG_AnimationDecoder) *) Returns a new
[IMG_AnimationDecoder](IMG_AnimationDecoder), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

These animation types are currently supported:

- ANI
- APNG
- AVIFS
- GIF
- WEBP

These are the supported properties:

- [`IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING):
  the file to load, if an SDL_IOStream isn't being used. This is required
  if
  [`IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER`](IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER)
  isn't set.
- [`IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER`](IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_POINTER):
  an SDL_IOStream containing a series of images. This should not be closed
  until the animation decoder is closed. This is required if
  [`IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING)
  isn't set.
- [`IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN`](IMG_PROP_ANIMATION_DECODER_CREATE_IOSTREAM_AUTOCLOSE_BOOLEAN):
  true if closing the animation decoder should also close the associated
  SDL_IOStream.
- [`IMG_PROP_ANIMATION_DECODER_CREATE_TYPE_STRING`](IMG_PROP_ANIMATION_DECODER_CREATE_TYPE_STRING):
  the input file type, e.g. "webp", defaults to the file extension if
  [`IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING`](IMG_PROP_ANIMATION_DECODER_CREATE_FILENAME_STRING)
  is set.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationDecoder](IMG_CreateAnimationDecoder)
- [IMG_CreateAnimationDecoder_IO](IMG_CreateAnimationDecoder_IO)
- [IMG_GetAnimationDecoderFrame](IMG_GetAnimationDecoderFrame)
- [IMG_ResetAnimationDecoder](IMG_ResetAnimationDecoder)
- [IMG_CloseAnimationDecoder](IMG_CloseAnimationDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

