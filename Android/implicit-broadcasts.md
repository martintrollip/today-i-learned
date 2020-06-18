- Date : 2020-06-18
- Tags : #Android

## Implicit broadcasts

Some implicit broadcasts such as CONNECTIVITY_CHANGED are sent often.  Apps which have a static/implicit receiver declared for this in the manifest will wake up and see if they're interested in this event.   

This can result in poor system performance and battery life if many apps has to wake up that often. 

To combat this, beginning with Android 8.0 (API level 26), the system imposes additional restrictions on manifest-declared receivers. You cannot use the manifest to declare a receiver for most implicit broadcasts (broadcasts that don't target your app specifically). You can still use a context-registered receiver when the user is actively using your app.


Some implicit broadcasts has also been removed 
API 29: NETWORK_STATE_CHANGED_ACTION
API 24: ACTION_NEW_PICTURE and ACTION_NEW_VIDEO

[Broadcasts overview](https://developer.android.com/guide/components/broadcasts)
