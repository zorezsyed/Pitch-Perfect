import UIKit

class Daddy{
    var name = ""
    init(name: String){
        print("Daddy Init called")
        self.name = name
    }
    
    var angryMode = "super"
    
    func angry(){
        print("\(self.name) is \(angryMode) angry")
    }
    
}
let zia = Daddy(name: "Zia")
zia.angryMode
zia.angry()
