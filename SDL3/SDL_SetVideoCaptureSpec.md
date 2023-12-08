###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetVideoCaptureSpec

Set specification

## Syntax

```c
int SDL_SetVideoCaptureSpec(SDL_VideoCaptureDevice *device,
                            const SDL_VideoCaptureSpec *desired,
                            SDL_VideoCaptureSpec *obtained,
                            int allowed_changes);

```

## Function Parameters

|                         |                             |
| ----------------------- | --------------------------- |
| **device**              | opened video capture device |
| **desired**             | desired video capture spec  |
| **obtained**            | obtained video capture spec |
| **allowed_changes**     | allow changes or not        |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenVideoCapture](SDL_OpenVideoCapture.md)
* [SDL_OpenVideoCaptureWithSpec](SDL_OpenVideoCaptureWithSpec.md)
* [SDL_GetVideoCaptureSpec](SDL_GetVideoCaptureSpec.md)

----
[CategoryAPI](CategoryAPI.md)
