//
//  ViewController.swift
//  RasbperryIOS
//
//  Created by first on 2020/07/31.
//  Copyright © 2020 miztnishi. All rights reserved.
//

import UIKit
import Foundation

class ViewController: UIViewController {
    
    
    @IBOutlet weak var openBtn: UIButton!
    
    @IBOutlet weak var closeBtn: UIButton!
    
    var alertController: UIAlertController!
    let OK = "200"
    let NG = "500"
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        // Do any additional setup after loading the view.        
    }
    //アラート表示
    func alert(title:String, message:String) {
        alertController = UIAlertController(title: title,
                                   message: message,
                                   preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: "OK",
                                                style: .default,
                                                handler:{ (action: UIAlertAction!) -> Void in
                                                    self.openBtn.isEnabled = true
                                                    self.closeBtn.isEnabled = true
                                                    
        }))
        //背景色:httpStatus 青:200 赤:500
        var backColor:UIColor = .blue
        if(title != OK){backColor = .red}
        let subview = (alertController.view.subviews.first?.subviews.first?.subviews.first!)! as UIView
        //背景を少し透過
        subview.backgroundColor = backColor.withAlphaComponent(0.5)
        alertController.view.tintColor = UIColor.black
        present(alertController, animated: true)
    }

    //玄関開ける
    @IBAction func openDoor(_ sender: Any) {
        request(methods: "openDoor")
    }
    
    //玄関閉める
    @IBAction func closeDoor(_ sender: Any) {
        request(methods:"closeDoor")
    }
    
    
    func request(methods:String){
        closeBtn.isEnabled = false
        openBtn.isEnabled = false
        let url: URL = URL(string: "http://IP/\(methods)")!
        var request = URLRequest(url: url)
        request.timeoutInterval = 5
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
        var resData:String = ""
        var resStatus:Int = 0
        
        let task: URLSessionTask = URLSession.shared.dataTask(with: request, completionHandler: {data, response, error in
            
            //JSON変換
            do {
                if let error = error{
                    DispatchQueue.main.async {
                        self.alert(title: "error", message:error.localizedDescription)
                    }
                    return
                }
                    
                 let json = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.allowFragments) as! [String:Any]
                print(json["ret"]!)
              
                resData = (json["ret"] as? String)!
                resStatus = (response as? HTTPURLResponse)!.statusCode
                
                //アラートで表示
                DispatchQueue.main.async {
                    self.alert(title: String(resStatus), message: resData)
                }
            }
            catch {
                print(error)
            }
            
            
           })
            task.resume() //実行する
    }
}

