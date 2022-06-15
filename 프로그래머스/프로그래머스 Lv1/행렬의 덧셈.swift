func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    var answer: [[Int]] = []
    
    for (a1, a2) in zip(arr1, arr2) {
        var tmp: [Int] = []
        for (b1, b2) in zip(a1, a2) {
            tmp.append(b1+b2)
        }
        answer.append(tmp)
    }
    return answer
}

// FIXME: 이 부분 ..
func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    return zip(arr1, arr2).map{zip($0,$1).map{$0+$1}}
}