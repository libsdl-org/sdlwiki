###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Linked_Version

This function gets the version of the dynamically linked SDL_image library.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
const SDL_version * IMG_Linked_Version(void);
```

## Return Value

(const SDL_version *) Returns SDL_image version

## Remarks

it should NOT be used to fill a version structure, instead you should use
the SDL_IMAGE_VERSION() macro.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

