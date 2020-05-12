- Date : 2020-05-12
- Tags : #Apache

## Expressions

You can use expressions in Apache to validate conditions. 

Supported directives are `<If>`, `<ElseIf>` and `<Else>`.

The expression parser provides a number of variables of the form `%{HTTP_HOST}`.  

You can combine this with `=~` to check if the string matches a regular expression. Apache uses the Perl Compatible Regular Expression vocabulary

To check the User-Agent for example use

```
 <If "%{HTTP_USER_AGENT} =~ ^(?i)Android/[\\S].*$">
    # Logic goes here
 </If>
```

[New in httpd 2.4: If, ElseIf, and Else](https://blogs.apache.org/httpd/entry/new_in_httpd_2_4)

[Expressions in Apache HTTP Server](http://httpd.apache.org/docs/2.4/expr.html)

[Pearl Compatible Regular Expression](http://pcre.org/)

