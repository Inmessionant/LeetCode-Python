#### 参考引用



- [x] **Algorithm-Pattern: https://github.com/greyireland/algorithm-pattern**
- [x] **代码随想录: https://programmercarl.com/  --->>>  https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html**



------



#### 时间空间复杂度



**递归算法的时间复杂度 = 递归的次数 * 每次递归的时间复杂度**

**递归算法的空间复杂度 = 每次递归的空间复杂度 \* 递归深度**



------



#### 内存空间

![C++内存空间](./assets/20210309165950660.png)

- 栈区(Stack) ：由编译器自动分配释放，存放函数的参数值，局部变量的值等，其操作方式类似于数据结构中的栈
- 堆区(Heap) ：一般由程序员分配释放，若程序员不释放，程序结束时可能由OS收回
- 未初始化数据区(Uninitialized Data)： 存放未初始化的全局变量和静态变量
- 初始化数据区(Initialized Data)：存放已经初始化的全局变量和静态变量
- 程序代码区(Text)：存放函数体的二进制代码

代码区和数据区所占空间都是固定的，而且占用的空间非常小，那么看运行时消耗的内存主要看可变部分

在可变部分中，栈区间的数据在代码块执行结束之后，系统会自动回收，而堆区间数据是需要程序员自己回收，所以也就是造成内存泄漏的发源地



------



#### 内存对齐



- 平台原因：不是所有的硬件平台都能访问任意内存地址上的任意数据，某些硬件平台只能在某些地址处取某些特定类型的数据，否则抛出硬件异常，为了同一个程序可以在多平台运行，需要内存对齐；
- 硬件原因：经过内存对齐后，CPU访问内存的速度大大提升；



------



#### Q&A



- **在项目中遇到的最大的技术挑战是什么，而你是如果解决的（考察解决问题的能力）**
- **给出一个项目问题来让面试者分析**
- **快速学习的能力：如果快速学习一门新的技术或者语言**
- **工作之后发现自己和学校有什么差别（体现出自己思维方式和学习方法上的进步，而不是用了两三年的时间有多学了那些技术，因为互联网是不断变化的）**
- **为什么选择我们公司（技术氛围，职业发展，公司潜力）**
- **职业规划（尽量从技术角度）**
- **坚持最长的一件事情是什么**
- **期望薪资（薪酬福利待遇）**



------



#### 研发流程



```
需求文档 -> 拆解需求 -> 项目记录 -> 画架构图 -> 定义接口 -> 数据结构及算法 -> 可扩展性及维护 -> 部署能力 -> 设计评审 -> 写代码 -> 研发自测 -> 组件联调 -> 转测 -> code review  -> 合入主干 -> 版本发布
```

