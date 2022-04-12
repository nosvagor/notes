// function add(n1: number, n2: number) {
//   return n1 + n2
// }
//
// const num1 = 8
// const num2 = 2.8
//
// const res = add(num1, num2)
// console.log(res)

// const ADMIN = 0
// const READ_ONLY = 1
// const AUTHOR = 2
// Better: enum ⤵️

enum Role {
  ADMIN,
  READ_ONLY,
  AUTHOR,
}

const person2 = {
  name: 'Max',
  age: 40,
  hobbies: ['Sports', 'Cooking', 'Reading'],
  role: Role.ADMIN,
}

const person: {
  name: string
  age: number
  hobbies: string[]
  role: [number, string]
} = {
  name: 'Max',
  age: 40,
  hobbies: ['Sports', 'Cooking', 'Reading'],
  role: [2, 'author'],
}

person.role.push('admin') // pushing to tuples will still work
// person.role[1] = 10 // assinging wrong type is now caught

let favoriteActivities: string[]
favoriteActivities = ['Sports']

console.log(person.name)

// type methods automaically available if types are specified
for (const hobby of person.hobbies) {
  console.log(hobby.toUpperCase())
}

if (person2.role == Role.ADMIN) {
  console.log('person is an admin')
}
