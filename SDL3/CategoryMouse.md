# CategoryMouse

Any GUI application has to deal with the mouse, and SDL provides functions
to manage mouse input and the displayed cursor.

Most interactions with the mouse will come through the event subsystem.
Moving a mouse generates an
[SDL_EVENT_MOUSE_MOTION](SDL_EVENT_MOUSE_MOTION) event, pushing a button
generates [SDL_EVENT_MOUSE_BUTTON_DOWN](SDL_EVENT_MOUSE_BUTTON_DOWN), etc,
but one can also query the current state of the mouse at any time with
[SDL_GetMouseState](SDL_GetMouseState)().

For certain games, it's useful to disassociate the mouse cursor from mouse
input. An FPS, for example, would not want the player's motion to stop as
the mouse hits the edge of the window. For these scenarios, use
[SDL_SetWindowRelativeMouseMode](SDL_SetWindowRelativeMouseMode)(), which
hides the cursor, grabs mouse input to the window, and reads mouse input no
matter how far it moves.

Games that want the system to track the mouse but want to draw their own
cursor can use [SDL_HideCursor](SDL_HideCursor)() and
[SDL_ShowCursor](SDL_ShowCursor)(). It might be more efficient to let the
system manage the cursor, if possible, using
[SDL_SetCursor](SDL_SetCursor)() with a custom image made through
[SDL_CreateColorCursor](SDL_CreateColorCursor)(), or perhaps just a
specific system cursor from
[SDL_CreateSystemCursor](SDL_CreateSystemCursor)().

SDL can, on many platforms, differentiate between multiple connected mice,
allowing for interesting input scenarios and multiplayer games. They can be
enumerated with [SDL_GetMice](SDL_GetMice)(), and SDL will send
[SDL_EVENT_MOUSE_ADDED](SDL_EVENT_MOUSE_ADDED) and
[SDL_EVENT_MOUSE_REMOVED](SDL_EVENT_MOUSE_REMOVED) events as they are
connected and unplugged.

Since many apps only care about basic mouse input, SDL offers a virtual
mouse device for touch and pen input, which often can make a desktop
application work on a touchscreen phone without any code changes. Apps that
care about touch/pen separately from mouse input should filter out events
with a `which` field of
[SDL_TOUCH_MOUSEID](SDL_TOUCH_MOUSEID)/SDL_PEN_MOUSEID.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryMouse, CategoryAPIFunction -->
- [SDL_CaptureMouse](SDL_CaptureMouse)
- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)
- [SDL_CursorVisible](SDL_CursorVisible)
- [SDL_DestroyCursor](SDL_DestroyCursor)
- [SDL_GetCursor](SDL_GetCursor)
- [SDL_GetDefaultCursor](SDL_GetDefaultCursor)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)
- [SDL_GetMice](SDL_GetMice)
- [SDL_GetMouseFocus](SDL_GetMouseFocus)
- [SDL_GetMouseNameForID](SDL_GetMouseNameForID)
- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)
- [SDL_GetWindowMouseGrab](SDL_GetWindowMouseGrab)
- [SDL_GetWindowMouseRect](SDL_GetWindowMouseRect)
- [SDL_GetWindowRelativeMouseMode](SDL_GetWindowRelativeMouseMode)
- [SDL_HasMouse](SDL_HasMouse)
- [SDL_HideCursor](SDL_HideCursor)
- [SDL_SetCursor](SDL_SetCursor)
- [SDL_SetRelativeMouseTransform](SDL_SetRelativeMouseTransform)
- [SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)
- [SDL_SetWindowMouseRect](SDL_SetWindowMouseRect)
- [SDL_SetWindowRelativeMouseMode](SDL_SetWindowRelativeMouseMode)
- [SDL_ShowCursor](SDL_ShowCursor)
- [SDL_WarpMouseGlobal](SDL_WarpMouseGlobal)
- [SDL_WarpMouseInWindow](SDL_WarpMouseInWindow)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryMouse, CategoryAPIDatatype -->
- [SDL_Cursor](SDL_Cursor)
- [SDL_MouseButtonFlags](SDL_MouseButtonFlags)
- [SDL_MouseID](SDL_MouseID)
- [SDL_MouseMotionTransformCallback](SDL_MouseMotionTransformCallback)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryMouse, CategoryAPIStruct -->
- (none.)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryMouse, CategoryAPIEnum -->
- [SDL_MouseWheelDirection](SDL_MouseWheelDirection)
- [SDL_SystemCursor](SDL_SystemCursor)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryMouse, CategoryAPIMacro -->
- [SDL_TOUCH_MOUSEID](SDL_TOUCH_MOUSEID)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)

