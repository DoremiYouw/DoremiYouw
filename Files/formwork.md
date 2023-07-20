# Markdown基本要素

## 标题

### 三级标题

## 强调

*这会是 斜体 的文字*
_这会是 斜体 的文字_

**这会是 粗体 的文字**
__这会是 粗体 的文字__

_你也 **组合** 这些符号_

~~这个文字将会被横线删除~~

## 列表

- Item 1
- Item 2
  - Item 2a
  - Item 2b

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

## 添加图片

reflash icon: ![图片加载失败显示这段文字](/images/icon/reflash.png)

## 链接

[MyGitHub](https://github.com/DoremiYouw/DoremiYouw/tree/main)

## 引用

正如 Kanye West 所说：

> We're living the future so
> the present is our past.

## 分割线

---

DoremiYouw

---

## 代码

行内代码:`print('hello')`

代码块：
```javascript {.line-numbers}
a=1
print(a)
```

## 语法高亮

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

## 任务列表

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## 表格

First Header | Second Header
------------ | -------------
1.1 | 1.2
2.1 | 2.2

## emoji

:smile:
:fa-car:

## 上标

30^th^

## 下标

H~2~O

## 脚注

Content [^1]

[^1]: Hi! This is a footnote

## 缩略

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
The HTML specification
is maintained by the W3C.

## 标记

==marked==

## Admonition标题

!!! note This is the admonition title
    This is the admonition body

# 数学

[数学](https://katex.org/docs/supported.html)

正弦三角函数：$sin(x)$

##

$$f(x)=x^2 + sum(e^x)$$

$$\alpha + \beta + \gamma + \phi + 0.5\cdot\pi$$

$$\tag{123} x+y^{2x}$$

$$\frac {a+s} {c^{2x}}$$

$$\sum_{\substack{0<i<m\\0<j<n}}{i+j}$$

$$\sum_{\mathclap{0\le i\le m}}$$

$$\sum_{\mathclap{1\le i\le j\le n}} x_{ij}$$


$\because$
$\therefore$

# 图像

[图像](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/diagrams)

