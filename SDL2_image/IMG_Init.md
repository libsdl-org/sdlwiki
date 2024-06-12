###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Init

Initialize SDL_image.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
int IMG_Init(int flags);
```

## Function Parameters

|     |           |                                      |
| --- | --------- | ------------------------------------ |
| int | **flags** | initialization flags, OR'd together. |

## Return Value

(int) Returns all currently initialized flags.

## Remarks

This function loads dynamic libraries that SDL_image needs, and prepares
them for use. This must be the first function you call in SDL_image, and if
it fails you should not continue with the library.

Flags should be one or more flags from [IMG_InitFlags](IMG_InitFlags) OR'd
together. It returns the flags successfully initialized, or 0 on failure.

Currently, these flags are:

- [`IMG_INIT_JPG`](IMG_INIT_JPG)
- [`IMG_INIT_PNG`](IMG_INIT_PNG)
- [`IMG_INIT_TIF`](IMG_INIT_TIF)
- [`IMG_INIT_WEBP`](IMG_INIT_WEBP)
- [`IMG_INIT_JXL`](IMG_INIT_JXL)
- [`IMG_INIT_AVIF`](IMG_INIT_AVIF)

More flags may be added in a future SDL_image release.

This function may need to load external shared libraries to support various
codecs, which means this function can fail to initialize that support on an
otherwise-reasonable system if the library isn't available; this is not
just a question of exceptional circumstances like running out of memory at
startup!

Note that you may call this function more than once to initialize with
additional flags. The return value will reflect both new flags that
successfully initialized, and also include flags that had previously been
initialized as well.

As this will return previously-initialized flags, it's legal to call this
with zero (no flags set). This is a safe no-op that can be used to query
the current initialization state without changing it at all.

Since this returns previously-initialized flags as well as new ones, and
you can call this with zero, you should not check for a zero return value
to determine an error condition. Instead, you should check to make sure all
the flags you require are set in the return value. If you have a game with
data in a specific format, this might be a fatal error. If you're a generic
image displaying app, perhaps you are fine with only having JPG and PNG
support and can live without WEBP, even if you request support for
everything.

Unlike other SDL satellite libraries, calls to [IMG_Init](IMG_Init) do not
stack; a single call to [IMG_Quit](IMG_Quit)() will deinitialize everything
and does not have to be paired with a matching [IMG_Init](IMG_Init) call.
For that reason, it's considered best practices to have a single
[IMG_Init](IMG_Init) and [IMG_Quit](IMG_Quit) call in your program. While
this isn't required, be aware of the risks of deviating from that behavior.

After initializing SDL_image, the app may begin to load images into
SDL_Surfaces or SDL_Textures.

## Version

This function is available since SDL_image 2.0.0.

## See Also

- [IMG_Quit](IMG_Quit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

