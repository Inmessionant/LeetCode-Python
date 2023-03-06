------



### 参考引用



- [x] Algorithm-Pattern：https://github.com/greyireland/algorithm-pattern
- [x] 代码随想录：https://programmercarl.com/



------



### Regex



- Guide：https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md
- 练习网站：https://regex101.com/



```
- 正则表达式是大小写敏感，所以The不会匹配the；
```



#### 元字符

| 元字符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| .      | `.`匹配任意单个字符，但不匹配换行符                          |
|        | ".ar" => The **car par**ked in the **gar**age.               |
|        |                                                              |
| [ ]    | 方括号用来指定一个字符集，在方括号中使用连字符来指定字符集的范围，在方括号中的字符集不关心顺序 |
|        | "[Tt]he" => **The** car parked in **the** garage.            |
|        | 方括号的句号就表示句号，"ar[.]" => A garage is a good place to park a c**ar.** |
|        |                                                              |
| [^ ]   | 一般来说 `^` 表示一个字符串的开头，但它用在一个方括号的开头的时候，它表示这个字符集是否定的 |
|        | "[^c]ar" => The car **par**ked in the **gar**age.            |
|        |                                                              |
| *      | 在`*`之前的字符出现 >=0                                      |
|        | "[a-z]*" => **The car parked in the garage** #21.            |
|        | `*`字符和`.`字符搭配可以匹配所有的字符`.*`                   |
|        | `*`和表示匹配空格的符号`\s`连起来用，如表达式`\s*cat\s*`匹配0或更多个空格开头和0或更多个空格结尾的cat字符串 |
|        |                                                              |
| +      | `+`号之前的字符出现>=1                                       |
|        | "c.+t" => The fat **cat sat on the mat**.                    |
|        |                                                              |
| ?      | 元字符 `?` 标记在符号前面的字符为可选，即出现 0 或 1 次      |
|        | 表达式 `[T]?he` 匹配字符串 `he` 和 `The`，"[T]he" => **The** car is parked in the garage. |
|        |                                                              |
| {n,m}  | 在正则表达式中 `{}` 是一个量词，常用来限定一个或一组字符可以重复出现的次数 (n <= num <= m) |
|        | 表达式 `[0-9]{2,3}` 匹配最少 2 位最多 3 位 0~9 的数字："[0-9]{2,3}" => The number was 9.**999**7 but we rounded it off to **10**.0. |
|        | 可以省略第二个参数，`[0-9]{2,}` 匹配至少两位 0~9 的数字："[0-9]{2,}" => The number was 9.**9997** but we rounded it off to **10**.0. |
|        | 如果逗号也省略掉则表示重复固定的次数，`[0-9]{3}` 匹配3位数字："[0-9]{3}" => The number was 9.**999**7 but we rounded it off to 10.0. |
|        |                                                              |
| (...)  | `(...)` 中包含的内容将会被看成一个整体，和数学中小括号（ ）的作用相同 |
|        | (ab)*` 匹配连续出现 0 或更多个 `ab，如果没有使用 `(...)` ，那么表达式 `ab*` 将匹配连续出现 0 或更多个 `b`，`(...){n}` 则表示整个标群内的字符重复n次 |
|        | ()` 中用或字符 `|` 表示或`，`(c|g|p)ar` 匹配 `car` 或 `gar` 或 `par` |
|        |                                                              |
| \|     | 或运算符，匹配符号前或后的字符                               |
|        | "(T\|t)he\|car" => **The** **car** is parked in **the** garage. |
|        |                                                              |
| \      | 反斜线 `\` 在表达式中用于转码紧跟其后的字符。用于指定 `{ } [ ] / \ + * . $ ^ |?` 这些特殊字符，如果想要匹配这些特殊字符则要在其前面加上反斜线 `\` |
|        | "(f\|c\|m)at\.?" => The **fat cat** sat on the **mat.**      |
|        |                                                              |
| ^      | `^` 用来检查匹配的字符串是否在所匹配字符串的开头，例如，在 `abc` 中使用表达式 `^a` 会得到结果 `a`。但如果使用 `^b` 将匹配不到任何结果。因为在字符串 `abc` 中并不是以 `b` 开头 |
|        | "^(T\|t)he" => **The** car is parked in the garage.    `^(T|t)he` 匹配以 `The` 或 `the` 开头的字符串 |
|        |                                                              |
| $      | `$` 号用来匹配字符是否是最后一个                             |
|        | "(at\.)" => The fat c**at.** sat. on the m**at.** ，`(at\.)$` 匹配以 `at.` 结尾的字符串，"(at\.)" => The fat cat. sat. on the **mat.** |



**`？`的几种用法：**

- “?”元字符规定其前导对象必须在目标对象中连续出现**零次或一次**，如：abc(d)?可匹配abc和abcd；
- 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是**非贪婪**的，非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”；源字符串`str=“dxxddxxd”`中，`d\w*?`会匹配 dx,而`d\w*?d`会匹配 dxxd；





#### 字符集

正则表达式提供一些常用的字符集简写。如下:

| 简写 | 描述                                               |
| ---- | -------------------------------------------------- |
| .    | 除换行符外的所有字符                               |
| \w   | 匹配所有字母数字，等同于 `[a-zA-Z0-9_]`            |
| \W   | 匹配所有非字母数字，即符号，等同于： `[^\w]`       |
| \d   | 匹配数字： `[0-9]`                                 |
| \D   | 匹配非数字： `[^\d]`                               |
| \s   | 匹配所有空格字符，等同于： `[\t\n\f\r\p{Z}]`       |
| \S   | 匹配所有非空格字符： `[^\s]`                       |
| \f   | 匹配一个换页符                                     |
| \n   | 匹配一个换行符                                     |
| \r   | 匹配一个回车符                                     |
| \t   | 匹配一个制表符                                     |
| \v   | 匹配一个垂直制表符                                 |
| \p   | 匹配 CR/LF（等同于 `\r\n`），用来匹配 DOS 行终止符 |



```python
import re

patten = "[a-zA-Z]*(\d+)(\w+)"
str1 = "qwe1234azAA"
res = re.search(patten, str1)
print(res.group(), res.group(0), res.group(1), res.group(2))
# res.group(): qwe1234azAA 
# res.group(0): qwe1234azAA 
# res.group(1): 1234 
# res.group(2): azAA


Group用法：
	1.有几个()就有几个group；
	2.group() = group(0)表示全部匹配结果， group(1)表示第一个匹配块，以此类推；
```





------



### What the f*ck Python!



- [x] What the f*ck Python：https://github.com/robertparley/wtfpython-cn



------

