
const countAndSay = n => {
  let next = '1'
  for (let i=2; i<=n; i++) {
    base = next
    next = compressStr(base)
  }
  return next
};

const compressStr = ss => {
  let compressedStr = ''
  let count = 1
  let i = 0
  for (i=1; i<ss.length; i++) {
    if (ss[i] == ss[i-1]) {
      count ++;
    } else {
      compressedStr += count + ss[i-1]
      count = 1
    }
  }
  compressedStr += count + ss[i-1]
  return compressedStr
}

res = countAndSay(4)
console.log(res)