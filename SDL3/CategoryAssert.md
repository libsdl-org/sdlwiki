# CategoryAssert

A helpful assertion macro!

SDL assertions operate like your usual `assert` macro, but with some added
features:

- It uses a trick with the `sizeof` operator, so disabled assertions
  vaporize out of the compiled code, but variables only referenced in the
  assertion won't trigger compiler warnings about being unused.
- It is safe to use with a dangling-else: `if (x) SDL_assert(y); else
  do_something();`
- It works the same everywhere, instead of counting on various platforms'
  compiler and C runtime to behave.
- It provides multiple levels of assertion ([SDL_assert](SDL_assert),
  [SDL_assert_release](SDL_assert_release),
  [SDL_assert_paranoid](SDL_assert_paranoid)) instead of a single
  all-or-nothing option.
- It offers a variety of responses when an assertion fails (retry, trigger
  the debugger, abort the program, ignore the failure once, ignore it for
  the rest of the program's run).
- It tries to show the user a dialog by default, if possible, but the app
  can provide a callback to handle assertion failures however they like.
- It lets failed assertions be retried. Perhaps you had a network failure
  and just want to retry the test after plugging your network cable back
  in? You can.
- It lets the user ignore an assertion failure, if there's a harmless
  problem that one can continue past.
- It lets the user mark an assertion as ignored for the rest of the
  program's run; if there's a harmless problem that keeps popping up.
- It provides statistics and data on all failed assertions to the app.
- It allows the default assertion handler to be controlled with environment
  variables, in case an automated script needs to control it.

To use it: do a debug build and just sprinkle around tests to check your
code!

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryAssert, CategoryAPIFunction -->
- [SDL_GetAssertionHandler](SDL_GetAssertionHandler)
- [SDL_GetAssertionReport](SDL_GetAssertionReport)
- [SDL_GetDefaultAssertionHandler](SDL_GetDefaultAssertionHandler)
- [SDL_ReportAssertion](SDL_ReportAssertion)
- [SDL_ResetAssertionReport](SDL_ResetAssertionReport)
- [SDL_SetAssertionHandler](SDL_SetAssertionHandler)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryAssert, CategoryAPIDatatype -->
- [SDL_AssertionHandler](SDL_AssertionHandler)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryAssert, CategoryAPIStruct -->
- [SDL_AssertData](SDL_AssertData)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryAssert, CategoryAPIEnum -->
- [SDL_AssertState](SDL_AssertState)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryAssert, CategoryAPIMacro -->
- [SDL_assert](SDL_assert)
- [SDL_assert_always](SDL_assert_always)
- [SDL_ASSERT_LEVEL](SDL_ASSERT_LEVEL)
- [SDL_assert_paranoid](SDL_assert_paranoid)
- [SDL_assert_release](SDL_assert_release)
- [SDL_TriggerBreakpoint](SDL_TriggerBreakpoint)
<!-- END CATEGORY LIST -->


----
[CategoryAPICategory](CategoryAPICategory)

