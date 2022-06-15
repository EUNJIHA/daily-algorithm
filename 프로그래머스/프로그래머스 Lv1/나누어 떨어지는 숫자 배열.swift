import Foundation

// func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
//     var answer: [Int] = []
    
//     for a in arr {
//         if a % divisor == 0 {
//             answer.append(a)
//         }
//     }
//     if answer.isEmpty {
//         answer.append(-1)
//     }
//     return answer.sorted()
// }

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    let array = arr.sorted().filter{ $0 % divisor == 0 }
    return  array == [] ? [-1] : array
}

solution([5, 9, 7, 10], 5)
