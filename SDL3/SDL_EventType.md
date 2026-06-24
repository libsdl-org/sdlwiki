# SDL_EventType

The types of events that can be delivered.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef enum SDL_EventType
{
    SDL_EVENT_FIRST     = 0,     /**< Unused (do not remove) */

    /* Application events */
    SDL_EVENT_QUIT           = 0x100, /**< User-requested quit */

    /* These application events have special meaning on iOS and Android, see README-ios.md and README-android.md for details */
    SDL_EVENT_TERMINATING,      /**< The application is being terminated by the OS. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationWillTerminate()
                                     Called on Android in onDestroy()
                                */
    SDL_EVENT_LOW_MEMORY,       /**< The application is low on memory, free memory if possible. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationDidReceiveMemoryWarning()
                                     Called on Android in onTrimMemory()
                                */
    SDL_EVENT_WILL_ENTER_BACKGROUND, /**< The application is about to enter the background. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationWillResignActive()
                                     Called on Android in onPause()
                                */
    SDL_EVENT_DID_ENTER_BACKGROUND, /**< The application did enter the background and may not get CPU for some time. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationDidEnterBackground()
                                     Called on Android in onPause()
                                */
    SDL_EVENT_WILL_ENTER_FOREGROUND, /**< The application is about to enter the foreground. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationWillEnterForeground()
                                     Called on Android in onResume()
                                */
    SDL_EVENT_DID_ENTER_FOREGROUND, /**< The application is now interactive. This event must be handled in a callback set with SDL_AddEventWatch().
                                     Called on iOS in applicationDidBecomeActive()
                                     Called on Android in onResume()
                                */

    SDL_EVENT_LOCALE_CHANGED,  /**< The user's locale preferences have changed. */

    SDL_EVENT_SYSTEM_THEME_CHANGED, /**< The system theme changed */

    /* Display events */
    /* 0x150 was SDL_DISPLAYEVENT, reserve the number for sdl2-compat */
    SDL_EVENT_DISPLAY_ORIENTATION = 0x151,   /**< Display orientation has changed to data1 */
    SDL_EVENT_DISPLAY_ADDED,                 /**< Display has been added to the system */
    SDL_EVENT_DISPLAY_REMOVED,               /**< Display has been removed from the system */
    SDL_EVENT_DISPLAY_MOVED,                 /**< Display has changed position */
    SDL_EVENT_DISPLAY_DESKTOP_MODE_CHANGED,  /**< Display has changed desktop mode */
    SDL_EVENT_DISPLAY_CURRENT_MODE_CHANGED,  /**< Display has changed current mode */
    SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED, /**< Display has changed content scale */
    SDL_EVENT_DISPLAY_USABLE_BOUNDS_CHANGED, /**< Display has changed usable bounds */
    SDL_EVENT_DISPLAY_FIRST = SDL_EVENT_DISPLAY_ORIENTATION,
    SDL_EVENT_DISPLAY_LAST = SDL_EVENT_DISPLAY_USABLE_BOUNDS_CHANGED,

    /* Window events */
    /* 0x200 was SDL_WINDOWEVENT, reserve the number for sdl2-compat */
    /* 0x201 was SDL_SYSWMEVENT, reserve the number for sdl2-compat */
    SDL_EVENT_WINDOW_SHOWN = 0x202,     /**< Window has been shown */
    SDL_EVENT_WINDOW_HIDDEN,            /**< Window has been hidden */
    SDL_EVENT_WINDOW_EXPOSED,           /**< Window has been exposed and should be redrawn, and can be redrawn directly from event watchers for this event.
                                             data1 is 1 for live-resize expose events, 0 otherwise. */
    SDL_EVENT_WINDOW_MOVED,             /**< Window has been moved to data1, data2 */
    SDL_EVENT_WINDOW_RESIZED,           /**< Window has been resized to data1xdata2 */
    SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED,/**< The pixel size of the window has changed to data1xdata2 */
    SDL_EVENT_WINDOW_METAL_VIEW_RESIZED,/**< The pixel size of a Metal view associated with the window has changed */
    SDL_EVENT_WINDOW_MINIMIZED,         /**< Window has been minimized */
    SDL_EVENT_WINDOW_MAXIMIZED,         /**< Window has been maximized */
    SDL_EVENT_WINDOW_RESTORED,          /**< Window has been restored to normal size and position */
    SDL_EVENT_WINDOW_MOUSE_ENTER,       /**< Window has gained mouse focus */
    SDL_EVENT_WINDOW_MOUSE_LEAVE,       /**< Window has lost mouse focus */
    SDL_EVENT_WINDOW_FOCUS_GAINED,      /**< Window has gained keyboard focus */
    SDL_EVENT_WINDOW_FOCUS_LOST,        /**< Window has lost keyboard focus */
    SDL_EVENT_WINDOW_CLOSE_REQUESTED,   /**< The window manager requests that the window be closed */
    SDL_EVENT_WINDOW_HIT_TEST,          /**< Window had a hit test that wasn't SDL_HITTEST_NORMAL */
    SDL_EVENT_WINDOW_ICCPROF_CHANGED,   /**< The window's ICC profile has changed */
    SDL_EVENT_WINDOW_DISPLAY_CHANGED,   /**< Window has been moved to display data1 */
    SDL_EVENT_WINDOW_DISPLAY_SCALE_CHANGED, /**< Window display scale has been changed */
    SDL_EVENT_WINDOW_SAFE_AREA_CHANGED, /**< The window safe area has been changed */
    SDL_EVENT_WINDOW_OCCLUDED,          /**< The window has been occluded */
    SDL_EVENT_WINDOW_ENTER_FULLSCREEN,  /**< The window has entered fullscreen mode */
    SDL_EVENT_WINDOW_LEAVE_FULLSCREEN,  /**< The window has left fullscreen mode */
    SDL_EVENT_WINDOW_DESTROYED,         /**< The window with the associated ID is being or has been destroyed. If this message is being handled
                                             in an event watcher, the window handle is still valid and can still be used to retrieve any properties
                                             associated with the window. Otherwise, the handle has already been destroyed and all resources
                                             associated with it are invalid */
    SDL_EVENT_WINDOW_HDR_STATE_CHANGED, /**< Window HDR properties have changed */
    SDL_EVENT_WINDOW_SETTINGS_CHANGED,  /**< Window settings have changed (on visionOS) */
    SDL_EVENT_WINDOW_FIRST = SDL_EVENT_WINDOW_SHOWN,
    SDL_EVENT_WINDOW_LAST = SDL_EVENT_WINDOW_SETTINGS_CHANGED,

    /* Keyboard events */
    SDL_EVENT_KEY_DOWN        = 0x300, /**< Key pressed */
    SDL_EVENT_KEY_UP,                  /**< Key released */
    SDL_EVENT_TEXT_EDITING,            /**< Keyboard text editing (composition) */
    SDL_EVENT_TEXT_INPUT,              /**< Keyboard text input */
    SDL_EVENT_KEYMAP_CHANGED,          /**< Keymap changed due to a system event such as an
                                            input language or keyboard layout change. */
    SDL_EVENT_KEYBOARD_ADDED,          /**< A new keyboard has been inserted into the system */
    SDL_EVENT_KEYBOARD_REMOVED,        /**< A keyboard has been removed */
    SDL_EVENT_TEXT_EDITING_CANDIDATES, /**< Keyboard text editing candidates */
    SDL_EVENT_SCREEN_KEYBOARD_SHOWN,   /**< The on-screen keyboard has been shown */
    SDL_EVENT_SCREEN_KEYBOARD_HIDDEN,  /**< The on-screen keyboard has been hidden */

    /* Mouse events */
    SDL_EVENT_MOUSE_MOTION    = 0x400, /**< Mouse moved */
    SDL_EVENT_MOUSE_BUTTON_DOWN,       /**< Mouse button pressed */
    SDL_EVENT_MOUSE_BUTTON_UP,         /**< Mouse button released */
    SDL_EVENT_MOUSE_WHEEL,             /**< Mouse wheel motion */
    SDL_EVENT_MOUSE_ADDED,             /**< A new mouse has been inserted into the system */
    SDL_EVENT_MOUSE_REMOVED,           /**< A mouse has been removed */

    /* Joystick events */
    SDL_EVENT_JOYSTICK_AXIS_MOTION  = 0x600, /**< Joystick axis motion */
    SDL_EVENT_JOYSTICK_BALL_MOTION,          /**< Joystick trackball motion */
    SDL_EVENT_JOYSTICK_HAT_MOTION,           /**< Joystick hat position change */
    SDL_EVENT_JOYSTICK_BUTTON_DOWN,          /**< Joystick button pressed */
    SDL_EVENT_JOYSTICK_BUTTON_UP,            /**< Joystick button released */
    SDL_EVENT_JOYSTICK_ADDED,                /**< A new joystick has been inserted into the system */
    SDL_EVENT_JOYSTICK_REMOVED,              /**< An opened joystick has been removed */
    SDL_EVENT_JOYSTICK_BATTERY_UPDATED,      /**< Joystick battery level change */
    SDL_EVENT_JOYSTICK_UPDATE_COMPLETE,      /**< Joystick update is complete */

    /* Gamepad events */
    SDL_EVENT_GAMEPAD_AXIS_MOTION  = 0x650, /**< Gamepad axis motion */
    SDL_EVENT_GAMEPAD_BUTTON_DOWN,          /**< Gamepad button pressed */
    SDL_EVENT_GAMEPAD_BUTTON_UP,            /**< Gamepad button released */
    SDL_EVENT_GAMEPAD_ADDED,                /**< A new gamepad has been inserted into the system */
    SDL_EVENT_GAMEPAD_REMOVED,              /**< A gamepad has been removed */
    SDL_EVENT_GAMEPAD_REMAPPED,             /**< The gamepad mapping was updated */
    SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN,        /**< Gamepad touchpad was touched */
    SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION,      /**< Gamepad touchpad finger was moved */
    SDL_EVENT_GAMEPAD_TOUCHPAD_UP,          /**< Gamepad touchpad finger was lifted */
    SDL_EVENT_GAMEPAD_SENSOR_UPDATE,        /**< Gamepad sensor was updated */
    SDL_EVENT_GAMEPAD_UPDATE_COMPLETE,      /**< Gamepad update is complete */
    SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED,  /**< Gamepad Steam handle has changed */
    SDL_EVENT_GAMEPAD_CAPSENSE_TOUCH,       /**< Gamepad capsense was touched */
    SDL_EVENT_GAMEPAD_CAPSENSE_RELEASE,     /**< Gamepad capsense was released */

    /* Touch events */
    SDL_EVENT_FINGER_DOWN      = 0x700,
    SDL_EVENT_FINGER_UP,
    SDL_EVENT_FINGER_MOTION,
    SDL_EVENT_FINGER_CANCELED,

    /* Pinch events */
    SDL_EVENT_PINCH_BEGIN      = 0x710,     /**< Pinch gesture started */
    SDL_EVENT_PINCH_UPDATE,                 /**< Pinch gesture updated */
    SDL_EVENT_PINCH_END,                    /**< Pinch gesture ended */

    /* 0x800, 0x801, and 0x802 were the Gesture events from SDL2. Do not reuse these values! sdl2-compat needs them! */

    /* Clipboard events */
    SDL_EVENT_CLIPBOARD_UPDATE = 0x900, /**< The clipboard changed */

    /* Drag and drop events */
    SDL_EVENT_DROP_FILE        = 0x1000, /**< The system requests a file open */
    SDL_EVENT_DROP_TEXT,                 /**< text/plain drag-and-drop event */
    SDL_EVENT_DROP_BEGIN,                /**< A new set of drops is beginning (NULL filename) */
    SDL_EVENT_DROP_COMPLETE,             /**< Current set of drops is now complete (NULL filename) */
    SDL_EVENT_DROP_POSITION,             /**< Position while moving over the window */

    /* Audio hotplug events */
    SDL_EVENT_AUDIO_DEVICE_ADDED = 0x1100,  /**< A new audio device is available */
    SDL_EVENT_AUDIO_DEVICE_REMOVED,         /**< An audio device has been removed. */
    SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED,  /**< An audio device's format has been changed by the system. */

    /* Sensor events */
    SDL_EVENT_SENSOR_UPDATE = 0x1200,     /**< A sensor was updated */

    /* Pressure-sensitive pen events */
    SDL_EVENT_PEN_PROXIMITY_IN = 0x1300,  /**< Pressure-sensitive pen has become available */
    SDL_EVENT_PEN_PROXIMITY_OUT,          /**< Pressure-sensitive pen has become unavailable */
    SDL_EVENT_PEN_DOWN,                   /**< Pressure-sensitive pen touched drawing surface */
    SDL_EVENT_PEN_UP,                     /**< Pressure-sensitive pen stopped touching drawing surface */
    SDL_EVENT_PEN_BUTTON_DOWN,            /**< Pressure-sensitive pen button pressed */
    SDL_EVENT_PEN_BUTTON_UP,              /**< Pressure-sensitive pen button released */
    SDL_EVENT_PEN_MOTION,                 /**< Pressure-sensitive pen is moving on the tablet */
    SDL_EVENT_PEN_AXIS,                   /**< Pressure-sensitive pen angle/pressure/etc changed */

    /* Camera hotplug events */
    SDL_EVENT_CAMERA_DEVICE_ADDED = 0x1400,  /**< A new camera device is available */
    SDL_EVENT_CAMERA_DEVICE_REMOVED,         /**< A camera device has been removed. */
    SDL_EVENT_CAMERA_DEVICE_APPROVED,        /**< A camera device has been approved for use by the user. */
    SDL_EVENT_CAMERA_DEVICE_DENIED,          /**< A camera device has been denied for use by the user. */

    /* Notification events */
    SDL_EVENT_NOTIFICATION_ACTION_INVOKED = 0x1500, /**< A user response to a system notification was received. */

    /* Render events */
    SDL_EVENT_RENDER_TARGETS_RESET = 0x2000, /**< The render targets have been reset and their contents need to be updated */
    SDL_EVENT_RENDER_DEVICE_RESET, /**< The device has been reset and all textures need to be recreated */
    SDL_EVENT_RENDER_DEVICE_LOST, /**< The device has been lost and can't be recovered. */

    /* Reserved events for private platforms */
    SDL_EVENT_PRIVATE0 = 0x4000,
    SDL_EVENT_PRIVATE1,
    SDL_EVENT_PRIVATE2,
    SDL_EVENT_PRIVATE3,

    /* Internal events */
    SDL_EVENT_POLL_SENTINEL = 0x7F00, /**< Signals the end of an event poll cycle */

    /** Events SDL_EVENT_USER through SDL_EVENT_LAST are for your use,
     *  and should be allocated with SDL_RegisterEvents()
     */
    SDL_EVENT_USER    = 0x8000,

    /**
     *  This last event is only for bounding internal arrays
     */
    SDL_EVENT_LAST    = 0xFFFF,

    /* This just makes sure the enum is the size of Uint32 */
    SDL_EVENT_ENUM_PADDING = 0x7FFFFFFF

} SDL_EventType;
```

## Mapping SDL event types to structs

All events are delivered through the [SDL_Event](SDL_Event) union. One uses
this union by choosing the correct struct based on the union's `type` field.
So if you get an SDL_EVENT_KEY_DOWN type, you would want SDL_Event's `key`
field (like `event->key`), which is an [SDL_KeyboardEvent](SDL_KeyboardEvent)
struct.

For convenience, here's a mapping of all event types to their place in
SDL_Event. Some event types have no extra data than the event itself, like
SDL_EVENT_TERMINATING, etc. In those cases, the event field/struct is listed
as [SDL_CommonEvent](SDL_CommonEvent), which mostly just provides timestamps
for the event.

There are `_FIRST` and `_LAST` fields for each subsection of events, like
`SDL_EVENT_DISPLAY_FIRST` and `SDL_EVENT_DISPLAY_LAST`. These are not listed
in this table, as they are never sent as events and are only used to provide
logical groupings.

This is listed in alphabetical order by event type name, not enum value order.

| Type                                    | SDL_Event field | Event struct                                                     |
| --------------------------------------- | --------------- | ---------------------------------------------------------------- |
| SDL_EVENT_TERMINATING                   | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_LOW_MEMORY                    | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_WILL_ENTER_BACKGROUND         | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_DID_ENTER_BACKGROUND          | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_WILL_ENTER_FOREGROUND         | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_DID_ENTER_FOREGROUND          | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_LOCALE_CHANGED                | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_SYSTEM_THEME_CHANGED          | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_DISPLAY_ORIENTATION           | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_ADDED                 | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_REMOVED               | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_MOVED                 | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_DESKTOP_MODE_CHANGED  | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_CURRENT_MODE_CHANGED  | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_CONTENT_SCALE_CHANGED | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_DISPLAY_USABLE_BOUNDS_CHANGED | display         | [SDL_DisplayEvent](SDL_DisplayEvent)                             |
| SDL_EVENT_WINDOW_SHOWN                  | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_HIDDEN                 | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_EXPOSED                | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_MOVED                  | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_RESIZED                | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED     | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_METAL_VIEW_RESIZED     | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_MINIMIZED              | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_MAXIMIZED              | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_RESTORED               | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_MOUSE_ENTER            | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_MOUSE_LEAVE            | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_FOCUS_GAINED           | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_FOCUS_LOST             | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_CLOSE_REQUESTED        | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_HIT_TEST               | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_ICCPROF_CHANGED        | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_DISPLAY_CHANGED        | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_DISPLAY_SCALE_CHANGED  | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_SAFE_AREA_CHANGED      | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_OCCLUDED               | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_ENTER_FULLSCREEN       | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_LEAVE_FULLSCREEN       | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_DESTROYED              | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_HDR_STATE_CHANGED      | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_WINDOW_SETTINGS_CHANGED       | window          | [SDL_WindowEvent](SDL_WindowEvent)                               |
| SDL_EVENT_KEY_DOWN                      | key             | [SDL_KeyboardEvent](SDL_KeyboardEvent)                           |
| SDL_EVENT_KEY_UP                        | key             | [SDL_KeyboardEvent](SDL_KeyboardEvent)                           |
| SDL_EVENT_TEXT_EDITING                  | edit            | [SDL_TextEditingEvent](SDL_TextEditingEvent)                     |
| SDL_EVENT_TEXT_INPUT                    | input           | [SDL_TextInputEvent](SDL_TextInputEvent)                         |
| SDL_EVENT_KEYMAP_CHANGED                | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_KEYBOARD_ADDED                | kdevice         | [SDL_KeyboardDeviceEvent](SDL_KeyboardDeviceEvent)               |
| SDL_EVENT_KEYBOARD_REMOVED              | kdevice         | [SDL_KeyboardDeviceEvent](SDL_KeyboardDeviceEvent)               |
| SDL_EVENT_TEXT_EDITING_CANDIDATES       | edit_candidates | [SDL_TextEditingCandidatesEvent](SDL_TextEditingCandidatesEvent) |
| SDL_EVENT_SCREEN_KEYBOARD_SHOWN         | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_SCREEN_KEYBOARD_HIDDEN        | common          | [SDL_CommonEvent](SDL_CommonEvent)                               |
| SDL_EVENT_MOUSE_MOTION                  | motion          | [SDL_MouseMotionEvent](SDL_MouseMotionEvent)                     |
| SDL_EVENT_MOUSE_BUTTON_DOWN             | button          | [SDL_MouseButtonEvent](SDL_MouseButtonEvent)                     |
| SDL_EVENT_MOUSE_BUTTON_UP               | button          | [SDL_MouseButtonEvent](SDL_MouseButtonEvent)                     |
| SDL_EVENT_MOUSE_WHEEL                   | wheel           | [SDL_MouseWheelEvent](SDL_MouseWheelEvent)                       |
| SDL_EVENT_MOUSE_ADDED                   | mdevice         | [SDL_MouseDeviceEvent](SDL_MouseDeviceEvent)                     |
| SDL_EVENT_MOUSE_REMOVED                 | mdevice         | [SDL_MouseDeviceEvent](SDL_MouseDeviceEvent)                     |
| SDL_EVENT_JOYSTICK_AXIS_MOTION          | jaxis           | [SDL_JoyAxisEvent](SDL_JoyAxisEvent)                             |
| SDL_EVENT_JOYSTICK_BALL_MOTION          | jball           | [SDL_JoyBallEvent](SDL_JoyBallEvent)                             |
| SDL_EVENT_JOYSTICK_HAT_MOTION           | jhat            | [SDL_JoyHatEvent](SDL_JoyHatEvent)                               |
| SDL_EVENT_JOYSTICK_BUTTON_DOWN          | jbutton         | [SDL_JoyButtonEvent](SDL_JoyButtonEvent)                         |
| SDL_EVENT_JOYSTICK_BUTTON_UP            | jbutton         | [SDL_JoyButtonEvent](SDL_JoyButtonEvent)                         |
| SDL_EVENT_JOYSTICK_ADDED                | jdevice         | [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)                         |
| SDL_EVENT_JOYSTICK_REMOVED              | jdevice         | [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)                         |
| SDL_EVENT_JOYSTICK_BATTERY_UPDATED      | jbattery        | [SDL_JoyBatteryEvent](SDL_JoyBatteryEvent)                       |
| SDL_EVENT_JOYSTICK_UPDATE_COMPLETE      | jdevice         | [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)                         |
| SDL_EVENT_GAMEPAD_AXIS_MOTION           | gaxis           | [SDL_GamepadAxisEvent](SDL_GamepadAxisEvent)                     |
| SDL_EVENT_GAMEPAD_BUTTON_DOWN           | gbutton         | [SDL_GamepadButtonEvent](SDL_GamepadButtonEvent)                 |
| SDL_EVENT_GAMEPAD_BUTTON_UP             | gbutton         | [SDL_GamepadButtonEvent](SDL_GamepadButtonEvent)                 |
| SDL_EVENT_GAMEPAD_ADDED                 | gdevice         | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)                 |
| SDL_EVENT_GAMEPAD_REMOVED               | gdevice         | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)                 |
| SDL_EVENT_GAMEPAD_REMAPPED              | gdevice         | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)                 |
| SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN         | gtouchpad       | [SDL_GamepadTouchpadEvent](SDL_GamepadTouchpadEvent)             |
| SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION       | gtouchpad       | [SDL_GamepadTouchpadEvent](SDL_GamepadTouchpadEvent)             |
| SDL_EVENT_GAMEPAD_TOUCHPAD_UP           | gtouchpad       | [SDL_GamepadTouchpadEvent](SDL_GamepadTouchpadEvent)             |
| SDL_EVENT_GAMEPAD_SENSOR_UPDATE         | gsensor         | [SDL_GamepadSensorEvent](SDL_GamepadSensorEvent)                 |
| SDL_EVENT_GAMEPAD_UPDATE_COMPLETE       | gdevice         | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)                 |
| SDL_EVENT_GAMEPAD_STEAM_HANDLE_UPDATED  | gdevice         | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)                 |
| SDL_EVENT_GAMEPAD_CAPSENSE_TOUCH        | gcapsense       | [SDL_GamepadCapSenseEvent](SDL_GamepadCapSenseEvent)             |
| SDL_EVENT_GAMEPAD_CAPSENSE_RELEASE      | gcapsense       | [SDL_GamepadCapSenseEvent](SDL_GamepadCapSenseEvent)             |
| SDL_EVENT_FINGER_DOWN                   | tfinger         | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)                     |
| SDL_EVENT_FINGER_UP                     | tfinger         | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)                     |
| SDL_EVENT_FINGER_MOTION                 | tfinger         | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)                     |
| SDL_EVENT_FINGER_CANCELED               | tfinger         | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)                     |
| SDL_EVENT_PINCH_BEGIN                   | pinch           | [SDL_PinchFingerEvent](SDL_PinchFingerEvent)                     |
| SDL_EVENT_PINCH_UPDATE                  | pinch           | [SDL_PinchFingerEvent](SDL_PinchFingerEvent)                     |
| SDL_EVENT_PINCH_END                     | pinch           | [SDL_PinchFingerEvent](SDL_PinchFingerEvent)                     |
| SDL_EVENT_CLIPBOARD_UPDATE              | clipboard       | [SDL_ClipboardEvent](SDL_ClipboardEvent)                         |
| SDL_EVENT_DROP_FILE                     | drop            | [SDL_DropEvent](SDL_DropEvent)                                   |
| SDL_EVENT_DROP_TEXT                     | drop            | [SDL_DropEvent](SDL_DropEvent)                                   |
| SDL_EVENT_DROP_BEGIN                    | drop            | [SDL_DropEvent](SDL_DropEvent)                                   |
| SDL_EVENT_DROP_COMPLETE                 | drop            | [SDL_DropEvent](SDL_DropEvent)                                   |
| SDL_EVENT_DROP_POSITION                 | drop            | [SDL_DropEvent](SDL_DropEvent)                                   |
| SDL_EVENT_AUDIO_DEVICE_ADDED            | adevice         | [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)                     |
| SDL_EVENT_AUDIO_DEVICE_REMOVED          | adevice         | [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)                     |
| SDL_EVENT_AUDIO_DEVICE_FORMAT_CHANGED   | adevice         | [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)                     |
| SDL_EVENT_SENSOR_UPDATE                 | sensor          | [SDL_SensorEvent](SDL_SensorEvent)                               |
| SDL_EVENT_PEN_PROXIMITY_IN              | pproximity      | [SDL_PenProximityEvent](SDL_PenProximityEvent)                   |
| SDL_EVENT_PEN_PROXIMITY_OUT             | pproximity      | [SDL_PenProximityEvent](SDL_PenProximityEvent)                   |
| SDL_EVENT_PEN_DOWN                      | ptouch          | [SDL_PenTouchEvent](SDL_PenTouchEvent)                           |
| SDL_EVENT_PEN_UP                        | ptouch          | [SDL_PenTouchEvent](SDL_PenTouchEvent)                           |
| SDL_EVENT_PEN_BUTTON_DOWN               | pbutton         | [SDL_PenButtonEvent](SDL_PenButtonEvent)                         |
| SDL_EVENT_PEN_BUTTON_UP                 | pbutton         | [SDL_PenButtonEvent](SDL_PenButtonEvent)                         |
| SDL_EVENT_PEN_MOTION                    | pmotion         | [SDL_PenMotionEvent](SDL_PenMotionEvent)                         |
| SDL_EVENT_PEN_AXIS                      | paxis           | [SDL_PenAxisEvent](SDL_PenAxisEvent)                             |
| SDL_EVENT_CAMERA_DEVICE_ADDED           | cdevice         | [SDL_CameraDeviceEvent](SDL_CameraDeviceEvent)                   |
| SDL_EVENT_CAMERA_DEVICE_REMOVED         | cdevice         | [SDL_CameraDeviceEvent](SDL_CameraDeviceEvent)                   |
| SDL_EVENT_CAMERA_DEVICE_APPROVED        | cdevice         | [SDL_CameraDeviceEvent](SDL_CameraDeviceEvent)                   |
| SDL_EVENT_CAMERA_DEVICE_DENIED          | cdevice         | [SDL_CameraDeviceEvent](SDL_CameraDeviceEvent)                   |
| SDL_EVENT_NOTIFICATION_ACTION_INVOKED   | notification    | [SDL_NotificationEvent](SDL_NotificationEvent)                   |
| SDL_EVENT_RENDER_TARGETS_RESET          | render          | [SDL_RenderEvent](SDL_RenderEvent)                               |
| SDL_EVENT_RENDER_DEVICE_RESET           | render          | [SDL_RenderEvent](SDL_RenderEvent)                               |
| SDL_EVENT_RENDER_DEVICE_LOST            | render          | [SDL_RenderEvent](SDL_RenderEvent)                               |

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEvents](CategoryEvents)

