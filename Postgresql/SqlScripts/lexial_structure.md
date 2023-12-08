

String Constants With C-Style Escapes

| Backslash Escape Sequence         | Interpretation                                   |
|-----------------------------------|--------------------------------------------------|
| \b                                | backspace                                        |
| \f                                | form feed                                        |
| \n                                | newline                                          |
| \r                                | carriage return                                  |
| \t                                | tab                                              |
| \o, \oo, \ooo (o = 0–7)           | octal byte value                                 |
| \xh, \xhh (h = 0–9, A–F)          | hexadecimal byte value                           |
| \uxxxx, \Uxxxxxxxx (x = 0–9, A–F) | 16 or 32-bit hexadecimal Unicode character value |

For example, the string 'data' could be written
```shell
U&'d\0061t\+000061'
U&'\0441\043B\043E\043D'
U&'d!0061t!+000061' UESCAPE '!'
```

```shell
$function$
BEGIN
    RETURN ($1 ~ $q$[\t\r\n\v\\]$q$);
END;
$function$
```

Numeric constants are accepted in these general forms:
```shell
digits
digits.[digits][e[+-]digits]
[digits].digits[e[+-]digits]
digitse[+-]digits
```

Additionally, non-decimal integer constants are accepted in these forms:
```shell
0xhexdigits
0ooctdigits
0bbindigits
```

A constant of an arbitrary type can be entered using any one of the following notations:
```shell
type 'string'
'string'::type
CAST ( 'string' AS type )
```


