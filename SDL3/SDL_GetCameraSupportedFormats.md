###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCameraSupportedFormats

Get the list of native formats/sizes a camera supports.

## Header File

Defined in [<SDL3/SDL_camera.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_camera.h)

## Syntax

```c
const SDL_CameraSpec * const * SDL_GetCameraSupportedFormats(SDL_CameraID devid, int *count);
```

## Function Parameters

|                              |           |                                                                           |
| ---------------------------- | --------- | ------------------------------------------------------------------------- |
| [SDL_CameraID](SDL_CameraID) | **devid** | the camera device instance ID to query.                                   |
| int *                        | **count** | a pointer filled in with the number of elements in the list, may be NULL. |

## Return Value

(const [SDL_CameraSpec](SDL_CameraSpec) * const *) Returns a NULL
terminated array of pointers to [SDL_CameraSpec](SDL_CameraSpec) or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns a list of all formats and frame sizes that a specific camera
can offer. This is useful if your app can accept a variety of image formats
and sizes and so want to find the optimal spec that doesn't require
conversion.

This function isn't strictly required; if you call
[SDL_OpenCamera](SDL_OpenCamera) with a NULL spec, SDL will choose a native
format for you, and if you instead specify a desired format, it will
transparently convert to the requested format on your behalf.

If `count` is not NULL, it will be filled with the number of elements in
the returned array.

Note that it's legal for a camera to supply an empty list. This is what
will happen on Emscripten builds, since that platform won't tell _anything_
about available cameras until you've opened one, and won't even tell if
there _is_ a camera until the user has given you permission to check
through a scary warning popup.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCameras](SDL_GetCameras)
- [SDL_OpenCamera](SDL_OpenCamera)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCamera](CategoryCamera)

