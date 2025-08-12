###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetAnimationDecoderProperties

Get the properties of an animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_PropertiesID IMG_GetAnimationDecoderProperties(IMG_AnimationDecoder* decoder);


#define IMG_PROP_METADATA_IGNORE_PROPS_BOOLEAN                 "SDL_image.metadata.ignore_props"
#define IMG_PROP_METADATA_DESCRIPTION_STRING                   "SDL_image.metadata.description"
#define IMG_PROP_METADATA_COPYRIGHT_STRING                     "SDL_image.metadata.copyright"
#define IMG_PROP_METADATA_TITLE_STRING                         "SDL_image.metadata.title"
#define IMG_PROP_METADATA_AUTHOR_STRING                        "SDL_image.metadata.author"
#define IMG_PROP_METADATA_CREATION_TIME_STRING                 "SDL_image.metadata.creation_time"
#define IMG_PROP_METADATA_LOOP_COUNT_NUMBER                    "SDL_image.metadata.loop_count"
```

## Function Parameters

|                                                |             |                        |
| ---------------------------------------------- | ----------- | ---------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the animation decoder. |

## Return Value

(SDL_PropertiesID) Returns the properties ID of the animation decoder, or 0
if there are no properties; call SDL_GetError() for more information.

## Remarks

This function returns the properties of the animation decoder, which holds
information about the underlying image such as description, copyright text
and loop count.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationDecoder](IMG_CreateAnimationDecoder)
- [IMG_CreateAnimationDecoder_IO](IMG_CreateAnimationDecoder_IO)
- [IMG_CreateAnimationDecoderWithProperties](IMG_CreateAnimationDecoderWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

