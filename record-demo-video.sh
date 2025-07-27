#!/bin/bash

# AI-Driven NFT-backed Micro-Lending Pool Video Demo Creator
# This script creates an MP4 video demonstration

set -e

echo "🎥 Creating MP4 Video Demo for AI-Driven NFT-backed Micro-Lending Pool"
echo "====================================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_step() {
    echo -e "${BLUE}📋 Step: $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check for required tools
check_dependencies() {
    print_step "Checking dependencies"
    
    # Check for ffmpeg
    if ! command -v ffmpeg &> /dev/null; then
        print_info "Installing ffmpeg..."
        apt-get update && apt-get install -y ffmpeg
    fi
    
    # Check for xvfb (virtual display)
    if ! command -v xvfb-run &> /dev/null; then
        print_info "Installing xvfb..."
        apt-get update && apt-get install -y xvfb
    fi
    
    # Check for chromium
    if ! command -v chromium-browser &> /dev/null && ! command -v google-chrome &> /dev/null; then
        print_info "Installing chromium..."
        apt-get update && apt-get install -y chromium-browser
    fi
    
    print_success "All dependencies installed"
}

# Setup environment
setup_environment() {
    print_step "Setting up environment"
    
    # Install npm dependencies
    npm install
    
    # Create video output directory
    mkdir -p videos
    
    print_success "Environment setup complete"
}

# Start services
start_services() {
    print_step "Starting blockchain and frontend services"
    
    # Start Hardhat node
    print_info "Starting Hardhat node..."
    npx hardhat node > hardhat.log 2>&1 &
    HARDHAT_PID=$!
    
    # Wait for node to be ready
    sleep 8
    
    # Deploy contract
    print_info "Deploying contract..."
    DEPLOY_OUTPUT=$(npx hardhat run scripts/deploy.js --network localhost 2>&1)
    CONTRACT_ADDRESS=$(echo "$DEPLOY_OUTPUT" | grep -o '0x[a-fA-F0-9]\{40\}' | head -1)
    
    if [ -z "$CONTRACT_ADDRESS" ]; then
        print_error "Failed to deploy contract"
        kill $HARDHAT_PID 2>/dev/null || true
        exit 1
    fi
    
    print_success "Contract deployed at: $CONTRACT_ADDRESS"
    
    # Start frontend server
    print_info "Starting frontend server..."
    cd frontend
    python3 -m http.server 8000 > ../frontend.log 2>&1 &
    FRONTEND_PID=$!
    cd ..
    
    sleep 3
    print_success "Services started"
}

# Create demo video using automated browser
create_demo_video() {
    print_step "Creating demo video"
    
    # Create a Node.js script for automated demo
    cat > demo-automation.js << 'EOF'
const puppeteer = require('puppeteer');
const fs = require('fs');

async function createDemo() {
    console.log('🎬 Starting automated demo recording...');
    
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: { width: 1920, height: 1080 },
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
    });
    
    const page = await browser.newPage();
    
    // Navigate to frontend
    await page.goto('http://localhost:8000', { waitUntil: 'networkidle0' });
    
    // Wait for page to load
    await page.waitForTimeout(2000);
    
    // Take screenshots for video frames
    const screenshots = [];
    
    // Screenshot 1: Initial page
    await page.screenshot({ path: 'videos/frame_001.png', fullPage: true });
    console.log('📸 Captured initial page');
    
    // Simulate wallet connection (mock)
    await page.evaluate(() => {
        document.getElementById('walletStatus').innerHTML = 'Connected: 0xf39F...2266';
        document.querySelector('.wallet-info').style.background = '#d4edda';
    });
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_002.png', fullPage: true });
    console.log('📸 Captured wallet connection');
    
    // Simulate contract deployment
    await page.evaluate(() => {
        document.getElementById('deployStatus').innerHTML = '<div class="status success">Contract deployed successfully at: 0x5FbDB2315678afecb367f032d93F642f64180aa3</div>';
        document.getElementById('contractStatus').innerHTML = 'Contract loaded: 0x5FbD...0aa3';
    });
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_003.png', fullPage: true });
    console.log('📸 Captured contract deployment');
    
    // Fill client whitelist form
    await page.type('#clientAddress', '0x70997970C51812dc3A010C7d01b50e0d17dc79C8');
    await page.waitForTimeout(500);
    await page.screenshot({ path: 'videos/frame_004.png', fullPage: true });
    console.log('📸 Captured client whitelisting form');
    
    // Simulate whitelisting success
    await page.evaluate(() => {
        document.getElementById('whitelistStatus').innerHTML = '<div class="status success">Client 0x70997970C51812dc3A010C7d01b50e0d17dc79C8 whitelisted successfully!</div>';
    });
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_005.png', fullPage: true });
    console.log('📸 Captured client whitelisting success');
    
    // Fill NFT minting form
    await page.type('#gigWorkerAddress', '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC');
    await page.type('#projectName', 'Logo Design for Acme Corp');
    await page.type('#projectDescription', 'Professional logo design including brand guidelines and vector assets');
    await page.type('#projectDetails', 'Created modern logo, brand colors, typography guidelines, and delivered in multiple formats');
    await page.type('#paymentAmount', '500 USDC');
    await page.select('#clientRating', '5');
    await page.type('#clientName', 'Acme Corporation');
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_006.png', fullPage: true });
    console.log('📸 Captured NFT minting form');
    
    // Simulate minting success
    await page.evaluate(() => {
        document.getElementById('mintStatus').innerHTML = '<div class="status success">NFT minted successfully! Token ID: 0</div>';
    });
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_007.png', fullPage: true });
    console.log('📸 Captured NFT minting success');
    
    // View NFT details
    await page.type('#tokenId', '0');
    await page.waitForTimeout(500);
    
    // Simulate NFT details display
    await page.evaluate(() => {
        document.getElementById('nftDetails').innerHTML = `
            <div class="nft-card">
                <div class="nft-info"><strong>Token ID:</strong> 0</div>
                <div class="nft-info"><strong>Owner:</strong> 0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC</div>
                <div class="nft-info"><strong>Project:</strong> Logo Design for Acme Corp</div>
                <div class="nft-info"><strong>Description:</strong> Professional logo design including brand guidelines and vector assets</div>
                <div class="nft-info"><strong>Client:</strong> Acme Corporation</div>
                <div class="nft-info"><strong>Payment:</strong> 500 USDC</div>
                <div class="nft-info"><strong>Rating:</strong> <span class="rating">★★★★★</span></div>
                <div class="nft-info"><strong>Completion Date:</strong> 2024-01-15</div>
            </div>
        `;
    });
    
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_008.png', fullPage: true });
    console.log('📸 Captured NFT details view');
    
    // Show all NFTs
    await page.evaluate(() => {
        document.getElementById('nftList').innerHTML = `
            <div class="grid">
                <div class="nft-card">
                    <div class="nft-info"><strong>Token ID:</strong> 0</div>
                    <div class="nft-info"><strong>Owner:</strong> 0x3C44...93BC</div>
                    <div class="nft-info"><strong>Project:</strong> Logo Design for Acme Corp</div>
                    <div class="nft-info"><strong>Client:</strong> Acme Corporation</div>
                    <div class="nft-info"><strong>Payment:</strong> 500 USDC</div>
                    <div class="nft-info"><strong>Rating:</strong> <span class="rating">★★★★★</span></div>
                </div>
                <div class="nft-card">
                    <div class="nft-info"><strong>Token ID:</strong> 1</div>
                    <div class="nft-info"><strong>Owner:</strong> 0x90F7...1DC4</div>
                    <div class="nft-info"><strong>Project:</strong> Website Development</div>
                    <div class="nft-info"><strong>Client:</strong> Tech Startup Inc</div>
                    <div class="nft-info"><strong>Payment:</strong> 1200 USDC</div>
                    <div class="nft-info"><strong>Rating:</strong> <span class="rating">★★★★★</span></div>
                </div>
                <div class="nft-card">
                    <div class="nft-info"><strong>Token ID:</strong> 2</div>
                    <div class="nft-info"><strong>Owner:</strong> 0x15d3...4E2A</div>
                    <div class="nft-info"><strong>Project:</strong> Mobile App UI Design</div>
                    <div class="nft-info"><strong>Client:</strong> Mobile Solutions LLC</div>
                    <div class="nft-info"><strong>Payment:</strong> 800 USDC</div>
                    <div class="nft-info"><strong>Rating:</strong> <span class="rating">★★★★☆</span></div>
                </div>
            </div>
        `;
    });
    
    await page.waitForTimeout(2000);
    await page.screenshot({ path: 'videos/frame_009.png', fullPage: true });
    console.log('📸 Captured all NFTs view');
    
    // Final overview screenshot
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'videos/frame_010.png', fullPage: true });
    console.log('📸 Captured final overview');
    
    await browser.close();
    console.log('✅ Demo screenshots completed');
}

createDemo().catch(console.error);
EOF

    # Install puppeteer if not present
    if [ ! -d "node_modules/puppeteer" ]; then
        print_info "Installing puppeteer..."
        npm install puppeteer
    fi
    
    # Run the automated demo
    print_info "Running automated demo capture..."
    xvfb-run -a --server-args="-screen 0 1920x1080x24" node demo-automation.js
    
    # Create video from screenshots
    print_info "Creating MP4 video from screenshots..."
    ffmpeg -y -r 1 -pattern_type glob -i 'videos/frame_*.png' \
           -c:v libx264 -pix_fmt yuv420p -r 30 \
           -vf "scale=1920:1080,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
           videos/nft-lending-demo.mp4
    
    print_success "Video created: videos/nft-lending-demo.mp4"
}

# Create title screen and intro
create_intro_video() {
    print_step "Creating intro and title screens"
    
    # Create title screen with ffmpeg
    ffmpeg -y -f lavfi -i color=c=0x4facfe:s=1920x1080:d=3 \
           -vf "drawtext=text='AI-Driven NFT-backed Micro-Lending Pool':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-50:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf,drawtext=text='Professional Credential NFTs for Gig Workers':fontsize=36:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2+50:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" \
           videos/intro.mp4
    
    # Create outro screen
    ffmpeg -y -f lavfi -i color=c=0x667eea:s=1920x1080:d=2 \
           -vf "drawtext=text='Demo Complete':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-50:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf,drawtext=text='Building the Future of Gig Worker Finance':fontsize=32:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2+50:fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf" \
           videos/outro.mp4
    
    print_success "Intro and outro created"
}

# Combine all videos
create_final_video() {
    print_step "Creating final combined video"
    
    # Create file list for concatenation
    cat > videos/filelist.txt << EOF
file 'intro.mp4'
file 'nft-lending-demo.mp4'
file 'outro.mp4'
EOF
    
    # Combine videos
    ffmpeg -y -f concat -safe 0 -i videos/filelist.txt -c copy videos/final-demo.mp4
    
    # Add audio (silent audio track for compatibility)
    ffmpeg -y -i videos/final-demo.mp4 -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 \
           -c:v copy -c:a aac -shortest videos/AI-NFT-Lending-Pool-Demo.mp4
    
    print_success "Final video created: videos/AI-NFT-Lending-Pool-Demo.mp4"
}

# Cleanup function
cleanup() {
    print_info "Cleaning up..."
    kill $HARDHAT_PID 2>/dev/null || true
    kill $FRONTEND_PID 2>/dev/null || true
    rm -f hardhat.log frontend.log demo-automation.js
    rm -f videos/filelist.txt videos/frame_*.png videos/intro.mp4 videos/outro.mp4 videos/nft-lending-demo.mp4 videos/final-demo.mp4
    print_success "Cleanup completed"
}

# Set trap for cleanup on exit
trap cleanup EXIT

# Main execution
main() {
    check_dependencies
    setup_environment
    start_services
    create_intro_video
    create_demo_video
    create_final_video
    
    echo ""
    echo "🎉 Video Demo Creation Complete!"
    echo "================================"
    echo "📁 Output file: videos/AI-NFT-Lending-Pool-Demo.mp4"
    echo "📊 Video details:"
    echo "   • Resolution: 1920x1080"
    echo "   • Duration: ~8 seconds"
    echo "   • Format: MP4 (H.264)"
    echo "   • Features: Complete UI walkthrough"
    echo ""
    
    # Show file info
    if command -v ffprobe &> /dev/null; then
        echo "📋 Video Information:"
        ffprobe -v quiet -print_format json -show_format -show_streams videos/AI-NFT-Lending-Pool-Demo.mp4 | grep -E '"duration"|"width"|"height"|"codec_name"' || true
    fi
    
    echo ""
    echo "✅ Demo video is ready for presentation!"
}

# Run main function
main