#!/usr/bin/env python3

import os
import subprocess
import time
import json
from pathlib import Path

def create_demo_video():
    """Create an MP4 demo video for the AI-Driven NFT-backed Micro-Lending Pool project"""
    
    print("🎥 Creating AI-Driven NFT-backed Micro-Lending Pool Demo Video")
    print("=" * 70)
    
    # Create temporary directory for video assets
    temp_dir = Path("temp_video_assets")
    temp_dir.mkdir(exist_ok=True)
    
    # Video settings
    fps = 30
    width = 1920
    height = 1080
    
    # Create intro slide
    create_intro_slide(temp_dir, width, height)
    
    # Create project overview slide
    create_project_overview_slide(temp_dir, width, height)
    
    # Create smart contract slide
    create_smart_contract_slide(temp_dir, width, height)
    
    # Create frontend demo slide
    create_frontend_slide(temp_dir, width, height)
    
    # Create deployment demo slide
    create_deployment_slide(temp_dir, width, height)
    
    # Create testing slide
    create_testing_slide(temp_dir, width, height)
    
    # Create conclusion slide
    create_conclusion_slide(temp_dir, width, height)
    
    # Generate video
    generate_video(temp_dir, fps, width, height)
    
    # Cleanup
    cleanup_temp_files(temp_dir)
    
    print("✅ Demo video created successfully: demo-video.mp4")

def create_intro_slide(temp_dir, width, height):
    """Create intro slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x1a1a2e:size={width}x{height}:duration=10',
        '-vf', 
        "drawtext=text='AI-Driven NFT-backed Micro-Lending Pool':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=300:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='Professional Credential NFT System':fontcolor=0x667eea:fontsize=36:x=(w-text_w)/2:y=400:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Demo Presentation':fontcolor=0x764ba2:fontsize=24:x=(w-text_w)/2:y=480:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'intro.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_project_overview_slide(temp_dir, width, height):
    """Create project overview slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x16213e:size={width}x{height}:duration=15',
        '-vf', 
        "drawtext=text='Project Overview':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=100:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='• Blockchain-based credential verification':fontcolor=white:fontsize=32:x=100:y=250:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• NFT minting for completed projects':fontcolor=white:fontsize=32:x=100:y=320:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• AI-driven credit scoring':fontcolor=white:fontsize=32:x=100:y=390:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Micro-lending pool for gig workers':fontcolor=white:fontsize=32:x=100:y=460:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Built with Solidity and JavaScript':fontcolor=white:fontsize=32:x=100:y=530:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'overview.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_smart_contract_slide(temp_dir, width, height):
    """Create smart contract slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x0f3460:size={width}x{height}:duration=20',
        '-vf', 
        "drawtext=text='Smart Contract Features':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=80:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='ProfessionalCredentialNFT Contract':fontcolor=0xffd700:fontsize=32:x=100:y=200:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf," +
        "drawtext=text='• Mint NFTs for completed projects':fontcolor=white:fontsize=28:x=120:y=270:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Store project metadata on-chain':fontcolor=white:fontsize=28:x=120:y=320:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Track work history and ratings':fontcolor=white:fontsize=28:x=120:y=370:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Calculate creditworthiness scores':fontcolor=white:fontsize=28:x=120:y=420:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='• Enable lending pool participation':fontcolor=white:fontsize=28:x=120:y=470:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'contract.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_frontend_slide(temp_dir, width, height):
    """Create frontend demo slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x667eea:size={width}x{height}:duration=25',
        '-vf', 
        "drawtext=text='Web Frontend Demo':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=80:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='Modern Web Interface':fontcolor=white:fontsize=36:x=100:y=200:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='✓ Connect MetaMask Wallet':fontcolor=white:fontsize=28:x=120:y=260:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='✓ Mint Professional Credential NFTs':fontcolor=white:fontsize=28:x=120:y=310:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='✓ View Work History and Ratings':fontcolor=white:fontsize=28:x=120:y=360:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='✓ Check Credit Score':fontcolor=white:fontsize=28:x=120:y=410:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='✓ Apply for Micro-loans':fontcolor=white:fontsize=28:x=120:y=460:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Built with HTML5, CSS3, JavaScript and Web3.js':fontcolor=0x1a1a2e:fontsize=24:x=(w-text_w)/2:y=550:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'frontend.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_deployment_slide(temp_dir, width, height):
    """Create deployment demo slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x1a1a2e:size={width}x{height}:duration=20',
        '-vf', 
        "drawtext=text='Deployment Process':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=80:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='npm install':fontcolor=0x00ff00:fontsize=32:x=100:y=200:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf," +
        "drawtext=text='Installing dependencies...':fontcolor=white:fontsize=24:x=120:y=240:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='npx hardhat compile':fontcolor=0x00ff00:fontsize=32:x=100:y=300:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf," +
        "drawtext=text='Compiling smart contracts...':fontcolor=white:fontsize=24:x=120:y=340:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='npx hardhat run scripts/deploy.js':fontcolor=0x00ff00:fontsize=32:x=100:y=400:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf," +
        "drawtext=text='Deploying to blockchain...':fontcolor=white:fontsize=24:x=120:y=440:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Contract deployed successfully!':fontcolor=0x00ff00:fontsize=28:x=100:y=500:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'deployment.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_testing_slide(temp_dir, width, height):
    """Create testing slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x764ba2:size={width}x{height}:duration=20',
        '-vf', 
        "drawtext=text='Testing and Demonstration':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=80:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='node scripts/test-mint.js':fontcolor=0x00ff00:fontsize=32:x=100:y=200:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf," +
        "drawtext=text='Minting test NFT...':fontcolor=white:fontsize=28:x=120:y=250:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Project: E-commerce Website Development':fontcolor=white:fontsize=24:x=120:y=300:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Rating: 4.8/5.0':fontcolor=white:fontsize=24:x=120:y=340:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Payment: $2,500':fontcolor=white:fontsize=24:x=120:y=380:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='NFT minted successfully!':fontcolor=0x00ff00:fontsize=28:x=120:y=440:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Token ID: 1 | Credit Score: 785':fontcolor=0xffd700:fontsize=24:x=120:y=480:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(temp_dir / 'testing.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def create_conclusion_slide(temp_dir, width, height):
    """Create conclusion slide"""
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=0x0f3460:size={width}x{height}:duration=10',
        '-vf', 
        "drawtext=text='Next Steps and Future Features':fontcolor=white:fontsize=56:x=(w-text_w)/2:y=80:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf," +
        "drawtext=text='AI Credit Scoring Algorithm':fontcolor=white:fontsize=32:x=100:y=200:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Automated Lending Pool':fontcolor=white:fontsize=32:x=100:y=250:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Mobile Application':fontcolor=white:fontsize=32:x=100:y=300:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Multi-chain Support':fontcolor=white:fontsize=32:x=100:y=350:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Integration with Gig Platforms':fontcolor=white:fontsize=32:x=100:y=400:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf," +
        "drawtext=text='Thank you for watching!':fontcolor=0xffd700:fontsize=48:x=(w-text_w)/2:y=500:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        str(temp_dir / 'conclusion.mp4')
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def generate_video(temp_dir, fps, width, height):
    """Combine all slides into final video"""
    print("🎬 Generating final video...")
    
    # Create concat file
    concat_file = temp_dir / 'concat.txt'
    with open(concat_file, 'w') as f:
        f.write(f"file '{temp_dir.absolute()}/intro.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/overview.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/contract.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/frontend.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/deployment.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/testing.mp4'\n")
        f.write(f"file '{temp_dir.absolute()}/conclusion.mp4'\n")
    
    # Combine videos
    cmd = [
        'ffmpeg', '-y',
        '-f', 'concat',
        '-safe', '0',
        '-i', str(concat_file),
        '-c', 'copy',
        'demo-video.mp4'
    ]
    subprocess.run(cmd, check=True, capture_output=True)

def cleanup_temp_files(temp_dir):
    """Clean up temporary files"""
    print("🧹 Cleaning up temporary files...")
    import shutil
    shutil.rmtree(temp_dir)

if __name__ == "__main__":
    create_demo_video()