#!/usr/bin/env python3

import subprocess
import os

def create_demo_video():
    """Create an ultra-simple MP4 demo video"""
    print("🎥 Creating AI-Driven NFT-backed Micro-Lending Pool Demo Video")
    print("=" * 70)
    
    # Video settings
    width = 1280
    height = 720
    
    # Slide 1: Title
    cmd1 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x1a1a2e:size={width}x{height}:duration=8',
        '-vf', 'drawtext=text="AI NFT Micro-Lending Pool":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=300,drawtext=text="Professional Credential System":fontcolor=0x667eea:fontsize=32:x=(w-text_w)/2:y=380',
        'slide1.mp4'
    ]
    
    # Slide 2: Overview
    cmd2 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x16213e:size={width}x{height}:duration=12',
        '-vf', 'drawtext=text="Project Overview":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=150,drawtext=text="Blockchain credential verification":fontcolor=white:fontsize=24:x=100:y=250,drawtext=text="NFT minting for projects":fontcolor=white:fontsize=24:x=100:y=300,drawtext=text="AI credit scoring":fontcolor=white:fontsize=24:x=100:y=350,drawtext=text="Micro-lending for gig workers":fontcolor=white:fontsize=24:x=100:y=400',
        'slide2.mp4'
    ]
    
    # Slide 3: Smart Contract
    cmd3 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x0f3460:size={width}x{height}:duration=15',
        '-vf', 'drawtext=text="Smart Contract":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=150,drawtext=text="ProfessionalCredentialNFT":fontcolor=0xffd700:fontsize=32:x=(w-text_w)/2:y=250,drawtext=text="Mint NFTs for work completion":fontcolor=white:fontsize=24:x=100:y=320,drawtext=text="Store metadata on blockchain":fontcolor=white:fontsize=24:x=100:y=370,drawtext=text="Calculate credit scores":fontcolor=white:fontsize=24:x=100:y=420',
        'slide3.mp4'
    ]
    
    # Slide 4: Frontend
    cmd4 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x667eea:size={width}x{height}:duration=15',
        '-vf', 'drawtext=text="Web Frontend":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=150,drawtext=text="Modern Web Interface":fontcolor=white:fontsize=32:x=(w-text_w)/2:y=250,drawtext=text="MetaMask Integration":fontcolor=white:fontsize=24:x=100:y=320,drawtext=text="NFT Minting Interface":fontcolor=white:fontsize=24:x=100:y=370,drawtext=text="Credit Score Display":fontcolor=white:fontsize=24:x=100:y=420',
        'slide4.mp4'
    ]
    
    # Slide 5: Demo
    cmd5 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x764ba2:size={width}x{height}:duration=12',
        '-vf', 'drawtext=text="Demo Results":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=150,drawtext=text="NFT Successfully Minted":fontcolor=0x00ff00:fontsize=32:x=(w-text_w)/2:y=250,drawtext=text="Project: Website Development":fontcolor=white:fontsize=24:x=100:y=320,drawtext=text="Rating: 4.8 out of 5":fontcolor=white:fontsize=24:x=100:y=370,drawtext=text="Credit Score: 785":fontcolor=0xffd700:fontsize=24:x=100:y=420',
        'slide5.mp4'
    ]
    
    # Slide 6: Future
    cmd6 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x0f3460:size={width}x{height}:duration=8',
        '-vf', 'drawtext=text="Future Features":fontcolor=white:fontsize=48:x=(w-text_w)/2:y=150,drawtext=text="AI Credit Algorithm":fontcolor=white:fontsize=28:x=100:y=250,drawtext=text="Automated Lending Pool":fontcolor=white:fontsize=28:x=100:y=300,drawtext=text="Mobile Application":fontcolor=white:fontsize=28:x=100:y=350,drawtext=text="Thank You!":fontcolor=0xffd700:fontsize=42:x=(w-text_w)/2:y=450',
        'slide6.mp4'
    ]
    
    # Create all slides
    commands = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6]
    
    print("Creating individual slides...")
    for i, cmd in enumerate(commands, 1):
        print(f"Creating slide {i}...")
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✅ Slide {i} created")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error creating slide {i}: {e}")
            return False
    
    # Create concat file
    print("Combining slides into final video...")
    with open('concat.txt', 'w') as f:
        for i in range(1, 7):
            f.write(f"file 'slide{i}.mp4'\n")
    
    # Combine all slides
    concat_cmd = [
        'ffmpeg', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'concat.txt',
        '-c', 'copy',
        'demo-video.mp4'
    ]
    
    try:
        subprocess.run(concat_cmd, check=True, capture_output=True)
        print("✅ Final video created: demo-video.mp4")
        
        # Cleanup temporary files
        print("🧹 Cleaning up...")
        for i in range(1, 7):
            os.remove(f'slide{i}.mp4')
        os.remove('concat.txt')
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error combining slides: {e}")
        return False

if __name__ == "__main__":
    success = create_demo_video()
    if success:
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
    else:
        print("\n❌ Failed to create demo video")