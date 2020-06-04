- Date : 2020-06-04
- Tags : #Android

## Static Views

Static views in Android can lead to memory leaks since it has a reference to the context.  Also a View is usually linked to a particular Activity so the architecture should not require a View to be declared static.

[Android – Why not to use static for View fields in your Activity or Fragments by Lars Vogel](http://blog.vogella.com/2013/03/12/android-why-not-to-use-static-for-view-fields-in-your-activity-or-fragments-by-lars-vogel/)

[Is it a good idea to declare static view in android?](https://stackoverflow.com/a/34107418/1859777)


