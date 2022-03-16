import Foundation
func converseNumber(_ n:Int, _ k: Int) -> String {
    var reverseBase: String = ""
    var quotient: Int = n
    var remainder: Int

    while quotient > 0 {
        (quotient, remainder) = quotient.quotientAndRemainder(dividingBy: k)
        reverseBase += String(remainder)
    }

    return String(reverseBase.reversed())
}
func isPrimeNumber(_ n:Int) -> Bool {
    if n == 1 { return false }
    for i in 2..<Int(sqrt(Double(n))) + 1 {
        if n % i == 0 { return false }
    }
    return true
}

func solution(_ n:Int, _ k:Int) -> Int {
    
    var answer = 0
    let strNumber = converseNumber(n, k)
    let candidates = strNumber.split(separator: "0").map { Int($0)! }
    
    for c in candidates {
        if isPrimeNumber(c) { answer += 1 }
    }
    
    return answer
}

print(solution(437674, 3))



import Foundation

func isPrimeNumber(_ n:Int) -> Bool {
    if n == 1 { return false }
    for i in 2..<Int(sqrt(Double(n))) + 1 {
        if n % i == 0 { return false }
    }
    return true
}

func solution(_ n:Int, _ k:Int) -> Int {
    
    var answer = 0
    let strNumber = String(n, radix: k)
    let candidates = strNumber.split(separator: "0").map { Int($0)! }
    
    for c in candidates {
        if isPrimeNumber(c) { answer += 1 }
    }
    
    return answer
}

print(solution(437674, 3))
