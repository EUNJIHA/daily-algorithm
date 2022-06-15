func solution(_ x:Int, _ n:Int) -> [Int64] {
    var answer: [Int64] = []

    for i in 0..<n {
        answer.append(Int64(x + x*i))
    }
    return answer
}

func solution(_ x:Int, _ n:Int) -> [Int64] {
    return Array(1...n).map { Int64($0 * x) }
}