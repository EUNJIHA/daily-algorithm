func solution(_ phone_number:String) -> String {
    let index = phone_number.index(phone_number.startIndex, offsetBy: phone_number.count - 4)
    return String(repeating: "*", count: phone_number.count - 4) + phone_number[index...]
}

func solution(_ phone_number:String) -> String {
    return String(repeating: "*", count: phone_number.count - 4) + phone_number.suffix(4)
}