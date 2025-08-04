#!/bin/bash

# AI-Driven NFT-backed Micro-Lending Pool Demo Runner
# This script automates the demo process

set -e

echo "🚀 Starting AI-Driven NFT-backed Micro-Lending Pool Demo"
echo "=================================================="

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

# Part 1: Environment Setup
print_step "Setting up environment"

print_info "Installing dependencies..."
npm install
print_success "Dependencies installed"

print_info "Project structure:"
if command -v tree &> /dev/null; then
    tree -I node_modules -L 2
else
    ls -la
fi

# Part 2: Smart Contract Overview
print_step "Showing smart contract details"

print_info "Smart Contract Code:"
echo "================================"
cat contracts/ProfessionalCredentialNFT.sol
echo "================================"

print_info "Sample Metadata Structure:"
echo "================================"
cat contracts/sample_metadata.json
echo "================================"

# Part 3: Start Local Blockchain
print_step "Starting local blockchain"

print_info "Starting Hardhat node..."
npx hardhat node > hardhat.log 2>&1 &
HARDHAT_PID=$!
print_success "Hardhat node started (PID: $HARDHAT_PID)"

# Wait for node to be ready
sleep 5

# Part 4: Deploy Contract
print_step "Deploying smart contract"

print_info "Deploying ProfessionalCredentialNFT contract..."
DEPLOY_OUTPUT=$(npx hardhat run scripts/deploy.js --network localhost)
CONTRACT_ADDRESS=$(echo "$DEPLOY_OUTPUT" | grep -o '0x[a-fA-F0-9]\{40\}')
print_success "Contract deployed at: $CONTRACT_ADDRESS"

# Part 5: Test Basic Functionality
print_step "Testing basic contract functionality"

print_info "Running test mint script..."
npx hardhat run scripts/test-mint.js --network localhost
print_success "Test minting completed"

# Part 6: Start Frontend Server
print_step "Starting frontend server"

print_info "Starting HTTP server for frontend..."
cd frontend
python3 -m http.server 8000 > ../frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
print_success "Frontend server started on http://localhost:8000 (PID: $FRONTEND_PID)"

# Part 7: Demo Instructions
print_step "Demo is ready!"

echo ""
echo "🎯 Demo Instructions:"
echo "===================="
echo "1. Open your browser to: http://localhost:8000"
echo "2. Make sure you have MetaMask installed and connected to localhost:8545"
echo "3. Import one of these test accounts into MetaMask:"
echo ""

# Extract test accounts from hardhat log
sleep 2
if [ -f hardhat.log ]; then
    echo "Test Accounts (with 10000 ETH each):"
    echo "====================================="
    grep -A 20 "Account #" hardhat.log | head -40
    echo ""
    echo "Private Keys:"
    echo "============="
    grep -A 20 "Private Key" hardhat.log | head -40
fi

echo ""
echo "🎬 Demo Walkthrough:"
echo "==================="
echo "1. Connect your wallet using one of the test accounts"
echo "2. Deploy the contract using the 'Deploy Contract' button"
echo "3. Whitelist a client address (use another test account)"
echo "4. Switch to the whitelisted client account in MetaMask"
echo "5. Mint credential NFTs using the form"
echo "6. View individual NFTs and browse all minted NFTs"
echo ""

echo "📊 Key Features to Demonstrate:"
echo "==============================="
echo "• Wallet connection and contract interaction"
echo "• Real-time transaction status updates"
echo "• Rich metadata display with ratings"
echo "• Responsive UI with modern design"
echo "• Complete gig worker credential system"
echo ""

echo "🔧 Technical Highlights:"
echo "========================"
echo "• ERC-721 NFT standard implementation"
echo "• Whitelisted client security model"
echo "• On-chain metadata storage"
echo "• Event-driven UI updates"
echo "• Gas-efficient contract design"
echo ""

echo "💡 Future Vision:"
echo "=================="
echo "• AI-powered credit scoring based on NFT history"
echo "• Dynamic interest rates based on reputation"
echo "• Integration with existing gig platforms"
echo "• Automated lending pool management"
echo ""

# Keep the demo running
echo "⏰ Demo is running. Press Ctrl+C to stop all services."
echo ""

# Function to cleanup on exit
cleanup() {
    print_info "Cleaning up demo services..."
    kill $HARDHAT_PID 2>/dev/null || true
    kill $FRONTEND_PID 2>/dev/null || true
    rm -f hardhat.log frontend.log
    print_success "Demo cleanup completed"
    exit 0
}

# Set trap for cleanup
trap cleanup SIGINT SIGTERM

# Wait for user to stop the demo
while true; do
    sleep 1
done