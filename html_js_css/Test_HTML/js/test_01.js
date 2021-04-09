// js循环

// while
/*
while(condition){
// 循环体
    }
*/
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}

// for循环
/*

for(表达式1，表达式2，表达式3){
    循环体
    }
表达式1: 循环开始之前执行
表达式2:循环的条件
表达式3:每一轮循环结束执行

 */

for (let i = 0; i < 10; i++) {
    console.log(i)
}

// for in: 遍历
const aList = Array(11, 22, 33, 44, 55);
for (i in aList) {
    console.log(i); // 得到数组的索引
    console.log(aList[i]); // 根据元素的下表获取其对应值
}

const obJA = {
    name: "Tom",
    age: 19,
    gender: "女"
}

for (i in obJA) {
    console.log(i); // 此处遍历得到的为对象的属性
    console.log(obJA[i])
}
