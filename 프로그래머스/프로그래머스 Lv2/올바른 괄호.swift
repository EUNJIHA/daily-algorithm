func solution(_ s:String) -> Bool
{
    var count = 0
    for a in s {
        if a == "("{
            count += 1
        }else{
            count -= 1
        }
        if count < 0 {
            break
        }
    }
    return count == 0 ? true : false
}

// func solution(_ s:String) -> Bool
// {
//     var answer: Bool = false
//     var stack: [Character] = []
    
//     var count: Int = 0
    
//     for i in s {
//         if i == "(" {
//             stack.append(i)
//             count += 1
//         }
//         else {
//             count -= 1
            
//             if stack.count > 0 && stack.last == "(" {
//                 stack.removeLast()
//             } else {stack.append(i)}
//         }
//         if count < 0 {
//             answer = false
//             break
//         }
//     }
//     return count < 0 ? false : stack.count == 0
// }