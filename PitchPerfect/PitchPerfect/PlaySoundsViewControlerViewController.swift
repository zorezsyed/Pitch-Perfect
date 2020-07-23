//
//  PlaySoundsViewControlerViewController.swift
//  PitchPerfect
//
//  Created by Zorez Syed on 7/3/20.
//  Copyright © 2020 Zorez Syed. All rights reserved.
//

import UIKit

class PlaySoundsViewControlerViewController: UIViewController {
    
    @IBOutlet weak var Slow: UIButton!
    @IBOutlet weak var Fast: UIButton!
    @IBOutlet weak var HighPitch: UIButton!
    @IBOutlet weak var LowPitch: UIButton!
    @IBOutlet weak var Echo: UIButton!
    @IBOutlet weak var Reverb: UIButton!

    var recordedAudioURL: URL!
    
    // MARK: Actions

    @IBAction func playSoundForButton(_ sender: UIButton) {
        print("Play Sound Button Pressed")
    }

    @IBAction func stopButtonPressed(_ sender: AnyObject) {
        print("Stop Audio Button Pressed")
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
