import Foundation

func solution(_ s:String) -> String {
//    var answer: String = ""
//
//    if s.count % 2 == 0 {
//
//        let startIndex = s.index(s.startIndex, offsetBy: Int(s.count / 2) - 1)
//        let endIndex = s.index(s.startIndex, offsetBy: Int(s.count / 2))
//        answer = String(s[startIndex...endIndex])
//    } else {
//        let index = s.index(s.startIndex, offsetBy: Int(s.count / 2))
//        answer = String(s[index])
//    }

    // return answer
    
    if Array(s).count % 2 == 0 {
         return String(Array(s)[(s.count/2)-1...(s.count/2)])
     }else{
         return String(Array(s)[s.count/2])
     }
}

print(solution("abcde"))
