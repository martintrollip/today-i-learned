- Date : 2020-05-08
- Tags : #Android

## Locate APK

You can locate the APK of an installed application on your device by using the following commands   

1. List the pacakages and look for the package name of the app you're looking for    
`adb shell pm list packages | sort`  

2. Find the apk path for that package    
`adb shell pm path com.the.package.you.want`  

3. Pull that path    
`adb pull /data/app/com.the.package.you.want-52332gsdsd32ew==/base.apk`  

**NOTE:** You might download it on one device but it might fail to install on another device due to missing libraries. This is since app bundles. You can't use this APK on devices with different architectures/configs.


