# CategorySharedObject

System-dependent library loading routines.

Shared objects are code that is programmatically loadable at runtime.
Windows calls these "DLLs", Linux calls them "shared libraries", etc.

To use them, build such a library, then call
[SDL_LoadObject](SDL_LoadObject)() on it. Once loaded, you can use
[SDL_LoadFunction](SDL_LoadFunction)() on that object to find the address
of its exported symbols. When done with the object, call
[SDL_UnloadObject](SDL_UnloadObject)() to dispose of it.

Some things to keep in mind:

- These functions only work on C function names. Other languages may have
  name mangling and intrinsic language support that varies from compiler to
  compiler.
- Make sure you declare your function pointers with the same calling
  convention as the actual library function. Your code will crash
  mysteriously if you do not do this.
- Avoid namespace collisions. If you load a symbol from the library, it is
  not defined whether or not it goes into the global symbol namespace for
  the application. If it does and it conflicts with symbols in your code or
  other shared libraries, you will not get the results you expect. :)
- Once a library is unloaded, all pointers into it obtained through
  [SDL_LoadFunction](SDL_LoadFunction)() become invalid, even if the
  library is later reloaded. Don't unload a library if you plan to use
  these pointers in the future. Notably: beware of giving one of these
  pointers to atexit(), since it may call that pointer after the library
  unloads.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySharedObject, CategoryAPIFunction -->
- [SDL_LoadFunction](SDL_LoadFunction)
- [SDL_LoadObject](SDL_LoadObject)
- [SDL_UnloadObject](SDL_UnloadObject)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySharedObject, CategoryAPIDatatype -->
- [SDL_SharedObject](SDL_SharedObject)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySharedObject, CategoryAPIStruct -->
- (none.)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySharedObject, CategoryAPIEnum -->
- (none.)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySharedObject, CategoryAPIMacro -->
- (none.)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)

