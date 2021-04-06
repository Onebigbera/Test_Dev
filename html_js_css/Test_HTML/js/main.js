// alert("Hello,JavaScript!")

// 声明变量同时赋值
const name = "Mike";

// 先声明，再赋值
let age;

age = 18;

// 未使用关键字的直接赋值，不能算作变量，其会变为windows的属性
gender = 20;
alert(window.gender)
alert(name)
alert(age)


console.log(name)
console.log(age)


let sex;
console.log(typeof name);
console.log(typeof age);
console.log(typeof gender);
console.log(typeof ture);
console.log(typeof sex);

// js中数据类型: 数字类型、字符串、数组、null、boolean、undefined

// 数字类类型
const b = 100;
const c = 10.666;

// 数组 Array: 类似与Python中的列表，可以通过下标取值
const aList = Array(1, 23, 4, 67);

// 属性 length: 返回数组的元素数量
alert(aList.length);

// 方法: push: 往数组最后插入元素
aList.push('Python');

// pop 获取数组中的最后一个元素
aList.pop()

// null: 空类型，类似与Python中的None
const d = null;

// undefined: 变量已声明，未赋值
let jack;
console.log(typeof jack);

// boolean: ture false
const t = true;
const f = false;

/*
    == 只比较内容是否相等，不管是不是同一个类型；
    === 不光内容相同，还会对比是否为相同的数值类型
*/

// 条件语句
const pen = 5;

if (pen > 5) {
    console.log("大于5")
} else if (pen === 5)
    console.log("等于5")
// 可以有多个 else if
else if (pen === 4)
    console.log("等于4")
else if (pen === 3)
    console.log("等于3")
else {
    console.log("不大于5")
}

// switch
const cup = 10, line = 20;

switch (line - cup) {
    case 10:
        console.log("相差为10");
        break;
    case 11:
        console.log("相差为11");
        break;
    // 默认要执行的部分
    default:
        console.log("上面的都没有匹配成功");


}


// 函数

// 定义函数
function func() {
    console.log("自定义函数执行");
}

// 调用函数
func();

// 带参数的函数
function add(var1, var2) {
    console.log(var1 + var2)
    return var2 - var1
}

const res = add(100, 120);
console.log(res)



