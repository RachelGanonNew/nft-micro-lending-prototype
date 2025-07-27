#!/usr/bin/env python3

import subprocess
import os

def create_demo_video():
    """Create a minimal MP4 demo video"""
    print("🎥 Creating AI-Driven NFT-backed Micro-Lending Pool Demo Video")
    print("=" * 70)
    
    # Video settings
    width = 1280
    height = 720
    
    # Slide 1: Title
    cmd1 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x1a1a2e:size={width}x{height}:duration=10',
        '-vf', 'drawtext=text="AI-Driven NFT-backed Micro-Lending Pool":fontcolor=white:fontsize=36:x=(w-text_w)/2:y=300,drawtext=text="Professional Credential NFT System":fontcolor=0x667eea:fontsize=24:x=(w-text_w)/2:y=360,drawtext=text="Demo Presentation":fontcolor=0x764ba2:fontsize=18:x=(w-text_w)/2:y=420',
        'slide1.mp4'
    ]
    
    # Slide 2: Overview
    cmd2 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x16213e:size={width}x{height}:duration=15',
        '-vf', 'drawtext=text="Project Overview":fontcolor=white:fontsize=42:x=(w-text_w)/2:y=100,drawtext=text="Blockchain-based credential verification":fontcolor=white:fontsize=20:x=80:y=200,drawtext=text="NFT minting for completed projects":fontcolor=white:fontsize=20:x=80:y=250,drawtext=text="AI-driven credit scoring":fontcolor=white:fontsize=20:x=80:y=300,drawtext=text="Micro-lending pool for gig workers":fontcolor=white:fontsize=20:x=80:y=350,drawtext=text="Built with Solidity and JavaScript":fontcolor=white:fontsize=20:x=80:y=400',
        'slide2.mp4'
    ]
    
    # Slide 3: Smart Contract
    cmd3 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x0f3460:size={width}x{height}:duration=18',
        '-vf', 'drawtext=text="Smart Contract Features":fontcolor=white:fontsize=42:x=(w-text_w)/2:y=100,drawtext=text="ProfessionalCredentialNFT Contract":fontcolor=0xffd700:fontsize=24:x=80:y=200,drawtext=text="Mint NFTs for completed projects":fontcolor=white:fontsize=18:x=100:y=260,drawtext=text="Store project metadata on-chain":fontcolor=white:fontsize=18:x=100:y=300,drawtext=text="Track work history and ratings":fontcolor=white:fontsize=18:x=100:y=340,drawtext=text="Calculate creditworthiness scores":fontcolor=white:fontsize=18:x=100:y=380,drawtext=text="Enable lending pool participation":fontcolor=white:fontsize=18:x=100:y=420',
        'slide3.mp4'
    ]
    
    # Slide 4: Frontend
    cmd4 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x667eea:size={width}x{height}:duration=20',
        '-vf', 'drawtext=text="Web Frontend Demo":fontcolor=white:fontsize=42:x=(w-text_w)/2:y=100,drawtext=text="Modern Web Interface":fontcolor=white:fontsize=28:x=80:y=180,drawtext=text="Connect MetaMask Wallet":fontcolor=white:fontsize=18:x=100:y=240,drawtext=text="Mint Professional Credential NFTs":fontcolor=white:fontsize=18:x=100:y=280,drawtext=text="View Work History and Ratings":fontcolor=white:fontsize=18:x=100:y=320,drawtext=text="Check Credit Score":fontcolor=white:fontsize=18:x=100:y=360,drawtext=text="Apply for Micro-loans":fontcolor=white:fontsize=18:x=100:y=400',
        'slide4.mp4'
    ]
    
    # Slide 5: Deployment
    cmd5 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x1a1a2e:size={width}x{height}:duration=18',
        '-vf', 'drawtext=text="Deployment Process":fontcolor=white:fontsize=42:x=(w-text_w)/2:y=100,drawtext=text="npm install":fontcolor=0x00ff00:fontsize=20:x=80:y=200,drawtext=text="Installing dependencies":fontcolor=white:fontsize=16:x=100:y=240,drawtext=text="npx hardhat compile":fontcolor=0x00ff00:fontsize=20:x=80:y=300,drawtext=text="Compiling smart contracts":fontcolor=white:fontsize=16:x=100:y=340,drawtext=text="npx hardhat run scripts/deploy.js":fontcolor=0x00ff00:fontsize=20:x=80:y=400,drawtext=text="Contract deployed successfully":fontcolor=0x00ff00:fontsize=18:x=80:y=460',
        'slide5.mp4'
    ]
    
    # Slide 6: Testing
    cmd6 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x764ba2:size={width}x{height}:duration=18',
        '-vf', 'drawtext=text="Testing and Demonstration":fontcolor=white:fontsize=42:x=(w-text_w)/2:y=100,drawtext=text="node scripts/test-mint.js":fontcolor=0x00ff00:fontsize=20:x=80:y=200,drawtext=text="Minting test NFT":fontcolor=white:fontsize=18:x=100:y=240,drawtext=text="Project: E-commerce Website Development":fontcolor=white:fontsize=16:x=100:y=290,drawtext=text="Rating: 4.8 out of 5.0":fontcolor=white:fontsize=16:x=100:y=330,drawtext=text="Payment: 2500 USD":fontcolor=white:fontsize=16:x=100:y=370,drawtext=text="NFT minted successfully":fontcolor=0x00ff00:fontsize=18:x=100:y=430',
        'slide6.mp4'
    ]
    
    # Slide 7: Conclusion
    cmd7 = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', f'color=c=0x0f3460:size={width}x{height}:duration=10',
        '-vf', 'drawtext=text="Next Steps and Future Features":fontcolor=white:fontsize=36:x=(w-text_w)/2:y=100,drawtext=text="AI Credit Scoring Algorithm":fontcolor=white:fontsize=20:x=80:y=200,drawtext=text="Automated Lending Pool":fontcolor=white:fontsize=20:x=80:y=240,drawtext=text="Mobile Application":fontcolor=white:fontsize=20:x=80:y=280,drawtext=text="Multi-chain Support":fontcolor=white:fontsize=20:x=80:y=320,drawtext=text="Integration with Gig Platforms":fontcolor=white:fontsize=20:x=80:y=360,drawtext=text="Thank you for watching!":fontcolor=0xffd700:fontsize=32:x=(w-text_w)/2:y=450',
        'slide7.mp4'
    ]
    
    # Create all slides
    commands = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7]
    
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
        for i in range(1, 8):
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
        for i in range(1, 8):
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
        print("⏱️  Duration: ~109 seconds")
        print("📺 Resolution: 1280x720")
        print("🎬 The video includes:")
        print("   - Project introduction and overview")
        print("   - Smart contract features explanation")
        print("   - Frontend demonstration")
        print("   - Deployment process walkthrough")
        print("   - Testing and minting demonstration")
        print("   - Future roadmap and conclusion")
    else:
        print("\n❌ Failed to create demo video")