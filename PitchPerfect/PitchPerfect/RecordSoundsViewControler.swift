//
//  RecordSoundsViewController.swift
//  PitchPerfect
//
//  Created by Zorez Syed on 7/1/20.
//  Copyright © 2020 Zorez Syed. All rights reserved.
//

import UIKit
import AVFoundation
var audioRecorder: AVAudioRecorder!
var audioPlayer: AVAudioPlayer!

class RecordSoundsViewController: UIViewController, AVAudioRecorderDelegate {

    
    @IBOutlet weak var recordingLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        stopRecordingButton.isEnabled = false
    }

    @IBAction func recordAudio(_ sender: AnyObject) {
        recordingLabel.text = "Recording"
        stopRecordingButton.isEnabled = true
        recordButton.isEnabled = false
        let dirPath = NSSearchPathForDirectoriesInDomains(.documentDirectory,.userDomainMask, true)[0] as String
        let recordingName = "recordedVoice.wav"
        let pathArray = [dirPath, recordingName]
        let filePath = URL(string: pathArray.joined(separator: "/"))

        let session = AVAudioSession.sharedInstance()
        try! session.setCategory(AVAudioSession.Category.playAndRecord, mode: AVAudioSession.Mode.default, options: AVAudioSession.CategoryOptions.defaultToSpeaker)

        try! audioRecorder = AVAudioRecorder(url: filePath!, settings: [:])
        audioRecorder.delegate=self
        audioRecorder.isMeteringEnabled = true
        audioRecorder.prepareToRecord()
        audioRecorder.record()
    }
    
    @IBOutlet weak var recordButton: UIButton!
    
    @IBAction func stopRecording(_ sender: AnyObject) {
        recordingLabel.text = "Tap to Record"
        stopRecordingButton.isEnabled = false
        recordButton.isEnabled = true
        audioRecorder.stop()
        let audioSession = AVAudioSession.sharedInstance()
        try! audioSession.setActive(false)
        print("Recording saved successfully at", audioRecorder.url)
//        do{
//            audioPlayer = try AVAudioPlayer(contentsOf: audioRecorder.url)
//            guard let player = audioPlayer else { return }
//            
//
//            player.prepareToPlay()
//            player.play()
//        }catch let error{
//            print(error.localizedDescription)
//        }
    }
    
    @IBOutlet weak var stopRecordingButton: UIButton!
        
    
    func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) {
        if flag {
            print("Sending file URL",audioRecorder.url)
            performSegue(withIdentifier: "stopRecording", sender:audioRecorder.url)
        } else {
            print("recording was not successful")
        }
    }
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "stopRecording"   {
            let playSoundsVC = segue.destination as! PlaySoundsViewController
            let recordedAudioURL = sender as! URL
            playSoundsVC.recordedAudioURL = recordedAudioURL
            print("setting URL in PlaySoundsViewController")
        }
    }
}

