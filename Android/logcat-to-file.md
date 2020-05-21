- Date : 2020-05-21
- Tags : #Android

## logcat to file


You can pipe a logcat output to a file using

```
  adb -d logcat <your package name>:<log level>  > cat.log
```

`-d` for actual device.  Use `-e` for emulator.

This is useful when Android Studios logcat viewer clears the logs on app crash for example. 


[logcat docs](https://developer.android.com/studio/command-line/logcat.html)

[logcat for your package](https://stackoverflow.com/questions/6854127/filter-logcat-to-get-only-the-messages-from-my-application-in-android)
