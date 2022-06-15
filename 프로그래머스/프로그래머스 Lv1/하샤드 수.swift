func solution(_ x:Int) -> Bool {
    return x % String(x).map {Int(String($0))!}.reduce(0, +) == 0
}

// Swift > String도 map 사용 가능. Character형을 Int로