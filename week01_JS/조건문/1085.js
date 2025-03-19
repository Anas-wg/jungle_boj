// 주어지는 (x,y) 에서 각각 x축, y축, 사각형 세로와의 거리, 사각형 가로와의 거리 중 최소를 리턴
const fs = require("fs")
const input = fs.readFileSync('input.txt').toString().trim().split(' ')

input_list = input.map((elems) => parseInt(elems))
let [x, y, w, h] = input_list
result_list = [x, y, w - x, h - y]


console.log(Math.min(...result_list))
