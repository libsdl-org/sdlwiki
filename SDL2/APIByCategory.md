# SDL 2.0 API by Category

## Basics

| **View information and functions related to...** | **View the header**                                                                |
| ------------------------------------------------ | -----------------------------------------------------------------------------------|
| [Initialization and Shutdown](CategoryInit)      | [SDL.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL.h)                 |
| [Configuration Variables](CategoryHints)         | [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)     |
| [Error Handling](CategoryError)                  | [SDL_error.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_error.h)     |
| [Log Handling](CategoryLog)                      | [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)         |
| [Assertions](CategoryAssert)                     | [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_assert.h)   |
| [Querying SDL Version](CategoryVersion)          | [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h) |


## Video

| **View information and functions related to...**        | **View the header**                                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------|
| [Display and Window Management](CategoryVideo)          | [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)         |
| [2D Accelerated Rendering](CategoryRender)              | [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)       |
| [Pixel Formats and Conversion Routines](CategoryPixels) | [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)       |
| [Rectangle Functions](CategoryRect)                     | [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)           |
| [Surface Creation and Simple Drawing](CategorySurface)  | [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)     |
| [Platform-specific Window Management](CategorySYSWM)    | [SDL_syswm.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_syswm.h)         |
| [Clipboard Handling](CategoryClipboard)                 | [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_clipboard.h) |
| [Vulkan Support](CategoryVulkan)                        | [SDL_vulkan.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_vulkan.h)       |
| [Metal Support](CategoryMetal)                          | [SDL_metal.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_metal.h)         |


## Input Events

| **View information and functions related to...**  | **View the header**                                                                              |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [Event Handling](CategoryEvents)                  | [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)                 |
| [Keyboard Support](CategoryKeyboard)              | [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h), [SDL_keycode.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keycode.h), [SDL_scancode.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_scancode.h) |
| [Mouse Support](CategoryMouse)                    | [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)                   |
| [Touch Support](CategoryTouch)                    | [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h)                   |
| [Joystick Support](CategoryJoystick)              | [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)             |
| [Game Controller Support](CategoryGameController) | [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h) |
| [Sensors](CategorySensor)                         | [SDL_sensor.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_sensor.h)                 |


## Force Feedback

| **View information and functions related to...** | **View the header**                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| [Force Feedback Support](CategoryHaptic)         | [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h) |


## Audio

| **View information and functions related to...**                | **View the header**                                                            |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [Audio Device Management, Playing and Recording](CategoryAudio) | [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h) |


## Threads

| **View information and functions related to...**   | **View the header**                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------- |
| [Thread Management](CategoryThread)                | [SDL_thread.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_thread.h) |
| [Thread Synchronization Primitives](CategoryMutex) | [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)   |
| [Atomic Operations](CategoryAtomic)                | [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h) |


## Timers

| **View information and functions related to...** | **View the header**                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------ |
| [Timer Support](CategoryTimer)                   | [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h) |


## File Abstraction

| **View information and functions related to...** | **View the header**                                                                      |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| [Filesystem Paths](CategoryFilesystem)           | [SDL_filesystem.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_filesystem.h) |
| [File I/O Abstraction](CategoryIO)               | [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)           |


## Shared Object Support

| **View information and functions related to...**                  | **View the header**                                                                               |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Shared Object Loading and Function Lookup](CategorySharedObject) | [SDL_loadso.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_loadso.h)                  |


## Platform and CPU Information

| **View information and functions related to...** | **View the header**                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| [Platform Detection](CategoryPlatform)           | [SDL_platform.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_platform.h) |
| [CPU Feature Detection](CategoryCPU)             | [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)   |
| [Byte Order and Byte Swapping](CategoryEndian)   | [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_endian.h)     |
| [Bit Manipulation](CategoryBits)                 | [SDL_bits.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_bits.h)         |


## Power Management

| **View information and functions related to...** | **View the header**                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------ |
| [Power Management Status](CategoryPower)         | [SDL_power.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_power.h) |


## Additional Functionality

| **View information and functions related to...**   | **View the header**                                                                      |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [Message boxes](CategoryMessageBox)                | [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h) |
| [Platform-specific Functionality](CategorySystem)  | [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)         |
| [Standard Library Functionality](CategoryStandard) | [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)         |

