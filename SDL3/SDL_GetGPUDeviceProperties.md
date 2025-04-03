# SDL_GetGPUDeviceProperties

Get the properties associated with a GPU device.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_PropertiesID SDL_GetGPUDeviceProperties(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                         |
| -------------------------------- | ---------- | ----------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

All properties are optional and may differ between GPU backends and SDL
versions.

The following properties are provided by SDL:

## Version

This function is available since SDL 3.4.0.

## [`SDL_PROP_GPU_DEVICE_NAME_STRING`](SDL_PROP_GPU_DEVICE_NAME_STRING)

Contains the name of the underlying device as reported by the system
driver. This string has no standardized format, is highly inconsistent
between hardware devices and drivers, and is able to change at any time. Do
not attempt to parse this string as it is bound to fail at some point in
the future when system drivers are updated, new hardware devices are
introduced, or when SDL adds new GPU backends or modifies existing ones.

Strings that have been found in the wild include:

- GTX 970
- GeForce GTX 970
- NVIDIA GeForce GTX 970
- Microsoft Direct3D12 (NVIDIA GeForce GTX 970)
- NVIDIA Graphics Device
- GeForce GPU
- P106-100
- AMD 15D8:C9
- AMD Custom GPU 0405
- AMD Radeon (TM) Graphics
- ASUS Radeon RX 470 Series
- Intel(R) Arc(tm) A380 Graphics (DG2)
- Virtio-GPU Venus (NVIDIA TITAN V)
- SwiftShader Device (LLVM 16.0.0)
- llvmpipe (LLVM 15.0.4, 256 bits)
- Microsoft Basic Render Driver
- unknown device

The above list shows that the same device can have different formats, the
vendor name may or may not appear in the string, the included vendor name
may not be the vendor of the chipset on the device, some manufacturers
include pseudo-legal marks while others don't, some devices may not use a
marketing name in the string, the device string may be wrapped by the name
of a translation interface, the device may be emulated in software, or the
string may contain generic text that does not identify the device at all.

###
[`SDL_PROP_GPU_DEVICE_DRIVER_NAME_STRING`](SDL_PROP_GPU_DEVICE_DRIVER_NAME_STRING)

Contains the self-reported name of the underlying system driver.

Strings that have been found in the wild include:

- Intel Corporation
- Intel open-source Mesa driver
- Qualcomm Technologies Inc. Adreno Vulkan Driver
- MoltenVK
- Mali-G715
- venus

###
[`SDL_PROP_GPU_DEVICE_DRIVER_VERSION_STRING`](SDL_PROP_GPU_DEVICE_DRIVER_VERSION_STRING)

Contains the self-reported version of the underlying system driver. This is
a relatively short version string in an unspecified format. If
[SDL_PROP_GPU_DEVICE_DRIVER_INFO_STRING](SDL_PROP_GPU_DEVICE_DRIVER_INFO_STRING)
is available then that property should be preferred over this one as it may
contain additional information that is useful for identifying the exact
driver version used.

Strings that have been found in the wild include:

- 53.0.0
- 0.405.2463
- 32.0.15.6614

###
[`SDL_PROP_GPU_DEVICE_DRIVER_INFO_STRING`](SDL_PROP_GPU_DEVICE_DRIVER_INFO_STRING)

Contains the detailed version information of the underlying system driver
as reported by the driver. This is an arbitrary string with no standardized
format and it may contain newlines. This property should be preferred over
[SDL_PROP_GPU_DEVICE_DRIVER_VERSION_STRING](SDL_PROP_GPU_DEVICE_DRIVER_VERSION_STRING)
if it is available as it usually contains the same information but in a
format that is easier to read.

Strings that have been found in the wild include:

- 101.6559
- 1.2.11
- Mesa 21.2.2 (LLVM 12.0.1)
- Mesa 22.2.0-devel (git-f226222 2022-04-14 impish-oibaf-ppa)
- v1.r53p0-00eac0.824c4f31403fb1fbf8ee1042422c2129

As well as the multiline string (which has a trailing newline):

```
Driver Build: 85da404, I46ff5fc46f, 1606794520
Date: 11/30/20
Compiler Version: EV031.31.04.01
Driver Branch: promo490_3_Google
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

