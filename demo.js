


big_list = [
  [1, 2, 3],
  [4, 4, 4]
]

res = big_list.map((single_list) => {
    return single_list.join('->')
})

console.log(res)