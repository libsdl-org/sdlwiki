# CategoryPen

Include file for SDL pen event handling.

This file describes operations for pressure-sensitive pen (stylus and/or
eraser) handling, e.g., for input and drawing tablets or suitably equipped
mobile / tablet devices.

To get started with pens:

- Listen to [SDL_PenMotionEvent](SDL_PenMotionEvent) and
  [SDL_PenButtonEvent](SDL_PenButtonEvent)
- To avoid treating pen events as mouse events, ignore
  [SDL_MouseMotionEvent](SDL_MouseMotionEvent) and
  [SDL_MouseButtonEvent](SDL_MouseButtonEvent) whenever `which` ==
  [SDL_PEN_MOUSEID](SDL_PEN_MOUSEID).

We primarily identify pens by [SDL_PenID](SDL_PenID). The implementation
makes a best effort to relate each [SDL_PenID](SDL_PenID) to the same
physical device during a session. Formerly valid [SDL_PenID](SDL_PenID)
values remain valid even if a device disappears.

For identifying pens across sessions, the API provides the type
[SDL_GUID](SDL_GUID) .

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryPen, CategoryAPIFunction -->
- [SDL_GetPenCapabilities](SDL_GetPenCapabilities)
- [SDL_GetPenFromGUID](SDL_GetPenFromGUID)
- [SDL_GetPenGUID](SDL_GetPenGUID)
- [SDL_GetPenName](SDL_GetPenName)
- [SDL_GetPens](SDL_GetPens)
- [SDL_GetPenStatus](SDL_GetPenStatus)
- [SDL_GetPenType](SDL_GetPenType)
- [SDL_PenConnected](SDL_PenConnected)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryPen, CategoryAPIDatatype -->
- (none.)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryPen, CategoryAPIStruct -->
- [SDL_PenCapabilityInfo](SDL_PenCapabilityInfo)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryPen, CategoryAPIEnum -->
- [SDL_PenAxis](SDL_PenAxis)
- [SDL_PenSubtype](SDL_PenSubtype)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryPen, CategoryAPIMacro -->
- (none.)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)

