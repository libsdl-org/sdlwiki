# SDL_CreateGPUXRSession

Creates an OpenXR session.

## Header File

Defined in [<SDL3/SDL_openxr.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_openxr.h)

## Syntax

```c
XrResult SDL_CreateGPUXRSession(SDL_GPUDevice *device, const XrSessionCreateInfo *createinfo, XrSession *session);
```

## Function Parameters

|                                  |                |                                                                          |
| -------------------------------- | -------------- | ------------------------------------------------------------------------ |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device**     | a GPU context.                                                           |
| const XrSessionCreateInfo *      | **createinfo** | the create info for the OpenXR session, sans the system ID.              |
| XrSession *                      | **session**    | a pointer filled in with an OpenXR session created for the given device. |

## Return Value

(XrResult) Returns the result of the call.

## Remarks

The OpenXR system ID is pulled from the passed GPU context.

## See Also

- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryOpenxr](CategoryOpenxr)

