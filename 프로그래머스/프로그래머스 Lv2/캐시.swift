func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    
    var answer = 0
    var cache : [String] = []
    
    for c in cities {
        let city = c.lowercased()
        if cache.contains(city) {
            cache.remove(at: cache.firstIndex(of: city)!)
            cache.append(city)
            answer += 1
        } else {
            if cache.count < cacheSize {
                cache.append(city)
            } else if cache.count > 0 {
                cache.removeFirst()
                cache.append(city)
            }
            answer += 5
        }
    }
    return answer
}
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))