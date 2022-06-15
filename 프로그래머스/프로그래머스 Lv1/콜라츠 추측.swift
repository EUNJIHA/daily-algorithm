func solution(_ num:Int) -> Int {
    var count: Int = 0
    var number: Int = num
    
    if number == 1 { return 0 }
    
    while count < 500 {
        count += 1
        
        if number % 2 == 0 { number /= 2 }
        else {number = number*3+1}
        
        if number == 1 { break }
    }
    
    return count == 500 ? -1 : count
}