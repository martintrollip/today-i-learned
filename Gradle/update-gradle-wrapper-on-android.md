- Date : 2020-06-10
- Tags : #Gradle

## Update Gradle wrapper on Android

Gradle build failing with:

```
Unzipping /Users/vagrant/.gradle/wrapper/dists/gradle-5.4.1-bin/d47no1zdn20orn3o5wz34tfzu/gradle-5.4.1-bin.zip to /Users/vagrant/.gradle/wrapper/dists/gradle-5.4.1-bin/d47no1zdn20orn3o5wz34tfzu
Exception in thread "main" java.util.zip.ZipException: zip file is empty
```

If you run into this issue, it means the Gradle wrapper jar has not been upgraded along with the wrapper version. To fix it, run 

`./gradlew wrapper --gradle-version 5.4.1 --distribution-type bin`


