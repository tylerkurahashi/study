// setTimeout(
//     () => console.log('1 sec has passed.'),1000
// )

// console.log('setTimeout() was executed.')

const array1 = [0,1,2,3]
const array2 = array1.map((ele) => {
    console.log(`Converting ${ele}.`)
    return ele*10
})

console.log('Conversion of array has completed.',array2)