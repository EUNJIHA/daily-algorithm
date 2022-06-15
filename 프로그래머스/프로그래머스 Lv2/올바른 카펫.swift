import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var allNum: Int = (brown - 4) / 2
    var answer: Int = 0
    for i in 1..<allNum { // 1, 2
        if i * (allNum-i) == yellow {
            answer = i
            break
        }
    }

    return [allNum-answer+2, answer+2]
}