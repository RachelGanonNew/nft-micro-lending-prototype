# AI-Driven NFT-backed Micro-Lending Pool - Video Demo

## 🎥 Demo Video

**File:** `demo-video.mp4`  
**Duration:** 70 seconds  
**Resolution:** 1280x720 (HD)  
**Format:** MP4 (H.264)

### Video Contents

The demo video includes the following sections:

1. **Introduction** (8s)
   - Project title and overview
   - Professional Credential NFT System

2. **Project Overview** (12s)
   - Blockchain-based credential verification
   - NFT minting for completed projects
   - AI-driven credit scoring
   - Micro-lending pool for gig workers

3. **Smart Contract Features** (15s)
   - ProfessionalCredentialNFT contract
   - NFT minting functionality
   - On-chain metadata storage
   - Credit score calculation

4. **Web Frontend** (15s)
   - Modern web interface
   - MetaMask integration
   - NFT minting interface
   - Credit score display

5. **Demo Results** (12s)
   - Successful NFT minting
   - Sample project data
   - Rating and credit score

6. **Future Features** (8s)
   - AI credit algorithm
   - Automated lending pool
   - Mobile application

## 🚀 How to Run the Demo

### Prerequisites

```bash
# Install Node.js dependencies
npm install

# Install system dependencies (if needed)
sudo apt update
sudo apt install -y ffmpeg
```

### Running the Project

1. **Compile Smart Contracts**
   ```bash
   npx hardhat compile
   ```

2. **Deploy to Local Network**
   ```bash
   npx hardhat node
   # In another terminal:
   npx hardhat run scripts/deploy.js --network localhost
   ```

3. **Test NFT Minting**
   ```bash
   node scripts/test-mint.js
   ```

4. **Open Frontend**
   ```bash
   # Open frontend/index.html in a web browser
   # Or serve with a local HTTP server:
   python3 -m http.server 8000
   # Then visit: http://localhost:8000/frontend/
   ```

### Recreating the Video

To recreate the demo video:

```bash
python3 final-video-creator.py
```

This will generate a new `demo-video.mp4` file with the same content.

## 📋 Project Structure

```
├── contracts/
│   ├── ProfessionalCredentialNFT.sol    # Main smart contract
│   └── sample_metadata.json             # Sample NFT metadata
├── scripts/
│   ├── deploy.js                        # Deployment script
│   └── test-mint.js                     # Testing script
├── frontend/
│   └── index.html                       # Web interface
├── demo-video.mp4                       # Demo video (generated)
├── final-video-creator.py               # Video generation script
└── README.md                            # Main project README
```

## 🎯 Key Features Demonstrated

### Smart Contract
- **ERC-721 NFT Implementation**: Professional credentials as NFTs
- **Metadata Storage**: Project details, ratings, payments on-chain
- **Credit Scoring**: Algorithmic calculation based on work history
- **Lending Integration**: Foundation for micro-lending pool

### Frontend
- **Web3 Integration**: MetaMask wallet connection
- **Interactive UI**: Modern, responsive design
- **NFT Minting**: User-friendly interface for credential creation
- **Portfolio View**: Display of work history and ratings

### AI Credit Scoring (Future)
- **Machine Learning**: Analysis of work patterns and ratings
- **Risk Assessment**: Automated creditworthiness evaluation
- **Dynamic Scoring**: Real-time updates based on new projects

## 🔧 Technical Stack

- **Blockchain**: Ethereum (Hardhat development environment)
- **Smart Contracts**: Solidity
- **Frontend**: HTML5, CSS3, JavaScript, Web3.js
- **Video Creation**: FFmpeg, Python
- **Development**: Node.js, npm

## 📊 Demo Data

The video demonstrates minting an NFT with the following sample data:

- **Project**: E-commerce Website Development
- **Client Rating**: 4.8/5.0
- **Payment**: $2,500
- **Completion Time**: On schedule
- **Generated Credit Score**: 785

## 🚀 Future Roadmap

1. **AI Credit Scoring Algorithm**
   - Machine learning model for risk assessment
   - Integration with external data sources
   - Real-time score updates

2. **Automated Lending Pool**
   - Smart contract-based lending mechanism
   - Interest rate calculation based on credit scores
   - Automated loan approval and repayment

3. **Mobile Application**
   - Native iOS and Android apps
   - Push notifications for loan opportunities
   - Mobile-friendly NFT minting

4. **Multi-chain Support**
   - Deployment on multiple blockchains
   - Cross-chain credential verification
   - Lower transaction fees

## 📞 Contact

For questions about this demo or the project, please refer to the main README.md file or create an issue in the repository.

---

**Note**: This is a proof-of-concept demonstration. The video showcases the core functionality and vision for an AI-driven NFT-backed micro-lending platform for gig workers.