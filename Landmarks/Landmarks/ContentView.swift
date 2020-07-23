//
//  ContentView.swift
//  Landmarks
//
//  Created by Zorez Syed on 6/24/20.
//  Copyright © 2020 Zorez Syed. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            MapView()
                .edgesIgnoringSafeArea(.top)
                .frame(height: 300)
            CircleImage()
                .offset(y: -130)
                .padding(.bottom, -130)
            
            VStack(alignment: .leading) {
                Text("Turtle Rock")
                .font(.largeTitle)
                .fontWeight(.semibold)
                .foregroundColor(Color.red)
                HStack {
                    Text("Joshua Tree National Park")
                        .font(.subheadline)
                        .fontWeight(.semibold)
                        .foregroundColor(Color.black)
                    Spacer()
                    Text("California")
                        .font(.subheadline)
                        .fontWeight(.semibold)
                        .foregroundColor(Color.black)
                }
            }
            .padding()
            Text("Zorez is awesome")
            TextField("Enter your name here", text: /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Value@*/.constant("")/*@END_MENU_TOKEN@*/)
            
            HStack {
                Slider(value: /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Value@*/.constant(10)/*@END_MENU_TOKEN@*/)
                Spacer()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
