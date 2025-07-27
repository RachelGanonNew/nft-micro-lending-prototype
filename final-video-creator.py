#!/usr/bin/env python3

import subprocess
import os

def create_demo_video():
    """Create final MP4 demo video"""
    print("🎥 Creating AI-Driven NFT-backed Micro-Lending Pool Demo Video")
    print("=" * 70)
    
    # Create slides one by one
    slides = []
    
    # Slide 1: Title
    print("Creating slide 1: Title...")
    cmd1 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x1a1a2e:size=1280x720:duration=8', 
            '-vf', 'drawtext=text="AI NFT Micro-Lending Pool":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=300,drawtext=text="Professional Credential System":fontcolor=0x667eea:fontsize=32:x=(w-text_w)/2:y=380', 
            'slide1.mp4']
    subprocess.run(cmd1, check=True, capture_output=True)
    slides.append('slide1.mp4')
    print("✅ Slide 1 created")
    
    # Slide 2: Overview
    print("Creating slide 2: Overview...")
    cmd2 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x16213e:size=1280x720:duration=12', 
            '-vf', 'drawtext=text="Project Overview":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=120,drawtext=text="Blockchain credential verification":fontcolor=white:fontsize=24:x=100:y=220,drawtext=text="NFT minting for projects":fontcolor=white:fontsize=24:x=100:y=270,drawtext=text="AI credit scoring":fontcolor=white:fontsize=24:x=100:y=320,drawtext=text="Micro-lending for gig workers":fontcolor=white:fontsize=24:x=100:y=370', 
            'slide2.mp4']
    subprocess.run(cmd2, check=True, capture_output=True)
    slides.append('slide2.mp4')
    print("✅ Slide 2 created")
    
    # Slide 3: Smart Contract
    print("Creating slide 3: Smart Contract...")
    cmd3 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x0f3460:size=1280x720:duration=15', 
            '-vf', 'drawtext=text="Smart Contract Features":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=120,drawtext=text="ProfessionalCredentialNFT":fontcolor=0xffd700:fontsize=32:x=(w-text_w)/2:y=220,drawtext=text="Mint NFTs for work completion":fontcolor=white:fontsize=24:x=100:y=290,drawtext=text="Store metadata on blockchain":fontcolor=white:fontsize=24:x=100:y=340,drawtext=text="Calculate credit scores":fontcolor=white:fontsize=24:x=100:y=390', 
            'slide3.mp4']
    subprocess.run(cmd3, check=True, capture_output=True)
    slides.append('slide3.mp4')
    print("✅ Slide 3 created")
    
    # Slide 4: Frontend
    print("Creating slide 4: Frontend...")
    cmd4 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x667eea:size=1280x720:duration=15', 
            '-vf', 'drawtext=text="Web Frontend":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=120,drawtext=text="Modern Web Interface":fontcolor=white:fontsize=32:x=(w-text_w)/2:y=220,drawtext=text="MetaMask Integration":fontcolor=white:fontsize=24:x=100:y=290,drawtext=text="NFT Minting Interface":fontcolor=white:fontsize=24:x=100:y=340,drawtext=text="Credit Score Display":fontcolor=white:fontsize=24:x=100:y=390', 
            'slide4.mp4']
    subprocess.run(cmd4, check=True, capture_output=True)
    slides.append('slide4.mp4')
    print("✅ Slide 4 created")
    
    # Slide 5: Demo Results
    print("Creating slide 5: Demo Results...")
    cmd5 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x764ba2:size=1280x720:duration=12', 
            '-vf', 'drawtext=text="Demo Results":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=120,drawtext=text="NFT Successfully Minted":fontcolor=0x00ff00:fontsize=32:x=(w-text_w)/2:y=220,drawtext=text="Project Website Development":fontcolor=white:fontsize=24:x=100:y=290,drawtext=text="Rating 4.8 out of 5":fontcolor=white:fontsize=24:x=100:y=340,drawtext=text="Credit Score 785":fontcolor=0xffd700:fontsize=24:x=100:y=390', 
            'slide5.mp4']
    subprocess.run(cmd5, check=True, capture_output=True)
    slides.append('slide5.mp4')
    print("✅ Slide 5 created")
    
    # Slide 6: Future Features
    print("Creating slide 6: Future Features...")
    cmd6 = ['ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=0x0f3460:size=1280x720:duration=8', 
            '-vf', 'drawtext=text="Future Features":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=120,drawtext=text="AI Credit Algorithm":fontcolor=white:fontsize=28:x=100:y=220,drawtext=text="Automated Lending Pool":fontcolor=white:fontsize=28:x=100:y=270,drawtext=text="Mobile Application":fontcolor=white:fontsize=28:x=100:y=320,drawtext=text="Thank You!":fontcolor=0xffd700:fontsize=42:x=(w-text_w)/2:y=420', 
            'slide6.mp4']
    subprocess.run(cmd6, check=True, capture_output=True)
    slides.append('slide6.mp4')
    print("✅ Slide 6 created")
    
    # Create concat file
    print("Combining slides into final video...")
    with open('concat.txt', 'w') as f:
        for slide in slides:
            f.write(f"file '{slide}'\n")
    
    # Combine all slides
    concat_cmd = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'concat.txt', '-c', 'copy', 'demo-video.mp4']
    subprocess.run(concat_cmd, check=True, capture_output=True)
    print("✅ Final video created: demo-video.mp4")
    
    # Cleanup temporary files
    print("🧹 Cleaning up...")
    for slide in slides:
        os.remove(slide)
    os.remove('concat.txt')
    
    return True

if __name__ == "__main__":
    try:
        create_demo_video()
        print("\n🎉 Demo video successfully created!")
        print("📁 File: demo-video.mp4")
        print("⏱️  Duration: ~70 seconds")
        print("📺 Resolution: 1280x720")
        print("🎬 The video demonstrates:")
        print("   - AI-driven NFT-backed micro-lending concept")
        print("   - Professional credential NFT system")
        print("   - Smart contract functionality")
        print("   - Web frontend interface")
        print("   - Demo results and future roadmap")
    except Exception as e:
        print(f"\n❌ Failed to create demo video: {e}")